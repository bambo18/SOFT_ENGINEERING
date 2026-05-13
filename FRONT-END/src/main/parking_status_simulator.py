# parking_status_simulator.py

import random
import time
from datetime import datetime


class ParkingSlot:

    def __init__(self, slot_id, location):
        self.slot_id = slot_id
        self.location = location
        self.status = "EMPTY"

    def update_status(self, distance_cm):

        # 차량이 가까우면 주차된 것으로 판단
        if distance_cm < 20:
            self.status = "OCCUPIED"
        else:
            self.status = "EMPTY"

    def get_status(self):
        return self.status


class Sensor:

    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def measure_distance(self):

        # 센서 거리 랜덤 생성
        return round(random.uniform(5, 100), 2)


class ParkingDatabase:

    def __init__(self):
        self.records = []

    def save_record(self, slot_id, status):

        record = {
            "slot_id": slot_id,
            "status": status,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.records.append(record)

        print(f"[DB] 저장 완료 -> {record}")

    def show_records(self):

        print("\n========== 저장된 기록 ==========")

        for record in self.records:
            print(record)

        print("================================\n")


# 시스템 실행
if __name__ == "__main__":

    sensor = Sensor("SENSOR-01")
    slot = ParkingSlot("A-01", "공학관 앞")
    database = ParkingDatabase()

    for _ in range(5):

        distance = sensor.measure_distance()

        print(f"\n[Sensor] 측정 거리: {distance} cm")

        slot.update_status(distance)

        print(f"[ParkingSlot] 현재 상태: {slot.get_status()}")

        database.save_record(
            slot.slot_id,
            slot.get_status()
        )

        time.sleep(1)

    database.show_records()