const express = require("express");
const app = express();

app.use(express.json());

let parkingSlots = [
  { parkingSlotId: "A-01", status: "empty", distanceCm: 30 },
  { parkingSlotId: "A-02", status: "occupied", distanceCm: 10 }
];

// 센서 데이터 수신
app.post("/api/parking/sensor", (req, res) => {
  const { parkingSlotId, status, distanceCm } = req.body;

  const slot = parkingSlots.find(s => s.parkingSlotId === parkingSlotId);
  if (slot) {
    slot.status = status;
    slot.distanceCm = distanceCm;
  }

  res.json({ message: "ok" });
});

// 프론트 조회
app.get("/api/parking/slots", (req, res) => {
  res.json(parkingSlots);
});

app.listen(8000, () => {
  console.log("Server running on port 8000");
});