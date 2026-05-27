package com.smartparking.backend.service;

import com.smartparking.backend.dto.ParkingStatusDTO;
import org.springframework.stereotype.Service;

@Service
public class ParkingSensorService {

    public ParkingStatusDTO updateParkingStatus(
            String slotId,
            Double distanceCm
    ) {

        String status;

        if (distanceCm <= 20.0) {
            status = "OCCUPIED";
        } else {
            status = "EMPTY";
        }

        return new ParkingStatusDTO(
                slotId,
                status,
                distanceCm
        );
    }
}