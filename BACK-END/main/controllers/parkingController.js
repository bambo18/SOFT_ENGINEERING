const parkingSlots = require("../data/parkingData");

const getParkingSlots = (req, res) => {
    res.json(parkingSlots);
};

const updateParkingSlot = (req, res) => {
    const { parkingSlotId, status, distanceCm } = req.body;

    const slot = parkingSlots.find(
        slot => slot.parkingSlotId === parkingSlotId
    );

    if (!slot) {
        return res.status(404).json({
            message: "Parking slot not found"
        });
    }

    slot.status = status;
    slot.distanceCm = distanceCm;

    return res.json({
        message: "Parking slot updated",
        slot
    });
};

module.exports = {
    getParkingSlots,
    updateParkingSlot
};