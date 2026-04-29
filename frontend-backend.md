# 프론트엔드 - 백엔드 연동 구조

## 사용 API

### 1. 센서 데이터 수신
POST /api/parking/sensor

### 2. 주차 상태 조회
GET /api/parking/slots

## 데이터 흐름
- 센서 → 서버 → DB 저장
- 프론트 → 서버 요청 → 상태 조회

## 특징
- REST API 기반 통신
- JSON 데이터 형식 사용