# API 명세서

## 주차 상태 전송 API

### POST /api/parking/sensor

### Request
{
  "parkingSlotId": "A-01",
  "deviceId": "raspi-01",
  "distanceCm": 10.5,
  "status": "occupied"
}

### Response
{
  "message": "ok"
}