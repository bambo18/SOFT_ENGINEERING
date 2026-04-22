const API_URL = "http://localhost:8000/api/parking/slots";

// API가 아직 없을 때 사용할 임시 데이터
const mockData = [
  { parkingSlotId: "A-01", status: "empty", distanceCm: 35.2 },
  { parkingSlotId: "A-02", status: "occupied", distanceCm: 8.4 },
  { parkingSlotId: "A-03", status: "empty", distanceCm: 30.1 },
  { parkingSlotId: "A-04", status: "occupied", distanceCm: 7.9 },
  { parkingSlotId: "B-01", status: "empty", distanceCm: 28.5 },
  { parkingSlotId: "B-02", status: "occupied", distanceCm: 10.3 }
];

const parkingGrid = document.getElementById("parkingGrid");
const totalCountEl = document.getElementById("totalCount");
const emptyCountEl = document.getElementById("emptyCount");
const occupiedCountEl = document.getElementById("occupiedCount");
const lastUpdatedEl = document.getElementById("lastUpdated");
const refreshBtn = document.getElementById("refreshBtn");

function getStatusText(status) {
  if (status === "empty") return "빈 자리";
  if (status === "occupied") return "사용 중";
  return "확인 불가";
}

function renderSlots(slots) {
  parkingGrid.innerHTML = "";

  slots.forEach((slot) => {
    const card = document.createElement("div");
    card.className = `slot-card ${slot.status || "unknown"}`;

    card.innerHTML = `
      <div class="slot-title">${slot.parkingSlotId}</div>
      <div class="slot-status">상태: ${getStatusText(slot.status)}</div>
      <div class="slot-distance">거리: ${slot.distanceCm ?? "-"} cm</div>
    `;

    parkingGrid.appendChild(card);
  });

  const total = slots.length;
  const empty = slots.filter((slot) => slot.status === "empty").length;
  const occupied = slots.filter((slot) => slot.status === "occupied").length;

  totalCountEl.textContent = total;
  emptyCountEl.textContent = empty;
  occupiedCountEl.textContent = occupied;

  const now = new Date();
  lastUpdatedEl.textContent = `마지막 갱신: ${now.toLocaleString("ko-KR")}`;
}

async function fetchParkingSlots() {
  try {
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error("API 호출 실패");
    }

    const data = await response.json();
    renderSlots(data);
  } catch (error) {
    console.warn("API 연결 실패, mock 데이터 사용:", error.message);
    renderSlots(mockData);
  }
}

refreshBtn.addEventListener("click", fetchParkingSlots);

fetchParkingSlots();