// 닫기 버튼
const closeButton = document.querySelector("#canvasClose button");
// 입력 영역
const openCanvas = document.querySelector("#openCanvas");

closeButton.addEventListener("click", (event) => {
  $(".card").hide();
  $("#openCanvas").show();
});

openCanvas.addEventListener("click", (event) => {
  $(".card").show();
  $("#openCanvas").hide();
});
