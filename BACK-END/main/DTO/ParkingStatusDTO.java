package com.smartparking.backend.dto;

public class ParkingStatusDTO {

    private String slotId;
    private String status;
    private Double distanceCm;

    public ParkingStatusDTO() {
    }

    public ParkingStatusDTO(String slotId, String status, Double distanceCm) {
        this.slotId = slotId;
        this.status = status;
        this.distanceCm = distanceCm;
    }

    public String getSlotId() {
        return slotId;
    }

    public void setSlotId(String slotId) {
        this.slotId = slotId;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Double getDistanceCm() {
        return distanceCm;
    }

    public void setDistanceCm(Double distanceCm) {
        this.distanceCm = distanceCm;
    }
}