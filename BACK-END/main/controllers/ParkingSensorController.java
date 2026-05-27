package com.smartparking.backend.controller;

import com.smartparking.backend.dto.ParkingStatusDTO;
import com.smartparking.backend.service.ParkingSensorService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/sensor")
public class ParkingSensorController {

    private final ParkingSensorService parkingSensorService;

    public ParkingSensorController(
            ParkingSensorService parkingSensorService
    ) {
        this.parkingSensorService = parkingSensorService;
    }

    @PostMapping("/status")
    public ParkingStatusDTO updateStatus(
            @RequestParam String slotId,
            @RequestParam Double distanceCm
    ) {

        return parkingSensorService.updateParkingStatus(
                slotId,
                distanceCm
        );
    }
}