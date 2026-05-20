package com.smartparking.service;

import com.smartparking.dto.ParkingSensorDto;
import org.springframework.stereotype.Service;

@Service
public class ParkingStatusService {

    public String updateParkingStatus(ParkingSensorDto dto) {

        if (dto.isOccupied()) {
            return dto.getSlotId() + " 주차 공간 사용 중";
        }

        return dto.getSlotId() + " 주차 공간 비어 있음";
    }
}