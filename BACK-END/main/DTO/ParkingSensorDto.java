package com.smartparking.dto;

public class ParkingSensorDto {

    private String sensorId;
    private String slotId;
    private double distanceCm;
    private boolean occupied;

    public ParkingSensorDto() {
    }

    public ParkingSensorDto(String sensorId, String slotId, double distanceCm, boolean occupied) {
        this.sensorId = sensorId;
        this.slotId = slotId;
        this.distanceCm = distanceCm;
        this.occupied = occupied;
    }

    public String getSensorId() {
        return sensorId;
    }

    public void setSensorId(String sensorId) {
        this.sensorId = sensorId;
    }

    public String getSlotId() {
        return slotId;
    }

    public void setSlotId(String slotId) {
        this.slotId = slotId;
    }

    public double getDistanceCm() {
        return distanceCm;
    }

    public void setDistanceCm(double distanceCm) {
        this.distanceCm = distanceCm;
    }

    public boolean isOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }
}