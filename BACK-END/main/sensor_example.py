import time
import json
from typing import Optional

import requests
import RPi.GPIO as GPIO


TRIG_PIN = 23
ECHO_PIN = 24

PARKING_SLOT_ID = "A-01"
DEVICE_ID = "raspi-slot-a01"

BACKEND_URL = "http://YOUR_SERVER_IP:8000/api/parking/sensor"
API_KEY = "YOUR_API_KEY"

MEASURE_INTERVAL_SECONDS = 5
OCCUPIED_DISTANCE_CM = 15.0
REQUEST_TIMEOUT_SECONDS = 5


def setup_gpio() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIG_PIN, False)
    time.sleep(2)


def cleanup_gpio() -> None:
    GPIO.cleanup()


def measure_distance_cm() -> Optional[float]:
    try:
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)

        pulse_start = time.time()
        timeout = pulse_start + 0.03

        while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()
            if pulse_start > timeout:
                return None

        pulse_end = time.time()
        timeout = pulse_end + 0.03

        while GPIO.input(ECHO_PIN) == 1:
            pulse_end = time.time()
            if pulse_end > timeout:
                return None

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        return round(distance, 2)

    except Exception:
        return None


def determine_status(distance_cm: Optional[float]) -> str:
    if distance_cm is None:
        return "unknown"
    if distance_cm <= OCCUPIED_DISTANCE_CM:
        return "occupied"
    return "empty"


def send_to_backend(distance_cm: Optional[float], status: str) -> None:
    payload = {
        "parkingSlotId": PARKING_SLOT_ID,
        "deviceId": DEVICE_ID,
        "distanceCm": distance_cm,
        "status": status,
        "measuredAt": int(time.time())
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY
    }

    response = requests.post(
        BACKEND_URL,
        headers=headers,
        data=json.dumps(payload),
        timeout=REQUEST_TIMEOUT_SECONDS
    )

    response.raise_for_status()
    print(f"[SUCCESS] sent: {payload}, response={response.status_code}")


def main() -> None:
    setup_gpio()

    try:
        while True:
            distance_cm = measure_distance_cm()
            status = determine_status(distance_cm)

            print(f"[INFO] distance={distance_cm}, status={status}")

            try:
                send_to_backend(distance_cm, status)
            except requests.RequestException as e:
                print(f"[ERROR] failed to send data: {e}")

            time.sleep(MEASURE_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\n[INFO] stopped by user")

    finally:
        cleanup_gpio()


if __name__ == "__main__":
    main()
