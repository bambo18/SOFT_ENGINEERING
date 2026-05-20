package com.smartparking.controller;

import com.smartparking.dto.ParkingSensorDto;
import com.smartparking.service.ParkingStatusService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/parking")
public class ParkingController {

    private final ParkingStatusService parkingStatusService;

    public ParkingController(ParkingStatusService parkingStatusService) {
        this.parkingStatusService = parkingStatusService;
    }

    @PostMapping("/sensor")
    public String receiveSensorData(@RequestBody ParkingSensorDto dto) {

        return parkingStatusService.updateParkingStatus(dto);
    }
}