public class ParkingSensorRequest {
    private String parkingSlotId;
    private String deviceId;
    private Double distanceCm;
    private String status;
    private Long measuredAt;

    public String getParkingSlotId() {
        return parkingSlotId;
    }

    public void setParkingSlotId(String parkingSlotId) {
        this.parkingSlotId = parkingSlotId;
    }

    public String getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(String deviceId) {
        this.deviceId = deviceId;
    }

    public Double getDistanceCm() {
        return distanceCm;
    }

    public void setDistanceCm(Double distanceCm) {
        this.distanceCm = distanceCm;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Long getMeasuredAt() {
        return measuredAt;
    }

    public void setMeasuredAt(Long measuredAt) {
        this.measuredAt = measuredAt;
    }
}