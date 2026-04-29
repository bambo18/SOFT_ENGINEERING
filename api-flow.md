# API 흐름 설계

## 전체 흐름

Sensor (Raspberry Pi)
        ↓
POST /api/parking/sensor
        ↓
Backend Server
        ↓
Database 저장
        ↓
GET /api/parking/slots
        ↓
Frontend 화면 표시

## 설명
- 센서는 주차 상태를 서버로 전송한다.
- 서버는 데이터를 저장하고 최신 상태를 관리한다.
- 프론트엔드는 서버로부터 데이터를 받아 화면에 표시한다.