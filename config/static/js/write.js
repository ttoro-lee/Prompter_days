// 캔버스
const canvasBody = document.querySelector(".card-body");
// 구분선
const line = document.querySelector(".m-0");
// 닫기 버튼
const closeButton = document.querySelector("#canvasClose button");
// 입력 영역
const input = document.querySelector("#user-input input");

closeButton.addEventListener("click", (event) => {
  $(".card-body").hide();
  $(".m-0").hide();
});

input.addEventListener("click", (event) => {
  $(".card-body").show();
  $(".m-0").show();
});
