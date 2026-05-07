const express = require("express");
const router = express.Router();

const {
    getParkingSlots,
    updateParkingSlot
} = require("../controllers/parkingController");

router.get("/slots", getParkingSlots);

router.post("/sensor", updateParkingSlot);

module.exports = router;