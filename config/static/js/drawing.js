const imageUpload = document.getElementById("imageUpload");
const drawButton = document.getElementById("drawButton");
const colorPicker = document.getElementById("colorPicker");
const eraseButton = document.getElementById("eraseButton");
const clearButton = document.getElementById("clearButton");
const storyButton = document.getElementById("storyButton");
const canvas = document.getElementById("drawingCanvas");
const context = canvas.getContext("2d");
let isDrawing = false;
let selectedColor = "black";
let erasing = false;

imageUpload.addEventListener("change", (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      const img = new Image();
      img.src = e.target.result;
      img.onload = () => {
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.drawImage(img, 0, 0, canvas.width, canvas.height);
      };
    };
    reader.readAsDataURL(file);
  }
});

drawButton.addEventListener("click", () => {
  canvas.addEventListener("mousedown", startDrawing);
  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mouseup", stopDrawing);
  canvas.addEventListener("mouseout", stopDrawing);
  colorPicker.style.display = "inline";
  eraseButton.style.display = "inline";
  clearButton.style.display = "inline";
});

function startDrawing(event) {
  isDrawing = true;
  context.beginPath();
  const x = event.clientX - canvas.getBoundingClientRect().left;
  const y = event.clientY - canvas.getBoundingClientRect().top;
  context.moveTo(x, y);
}

function draw(event) {
  if (!isDrawing) return;

  const x = event.clientX - canvas.getBoundingClientRect().left;
  const y = event.clientY - canvas.getBoundingClientRect().top;

  context.lineWidth = 2;
  context.lineCap = "round";
  context.strokeStyle = erasing ? "white" : selectedColor;

  context.lineTo(x, y);
  context.stroke();
  context.beginPath();
  context.moveTo(x, y);
}

function stopDrawing() {
  isDrawing = false;
  context.beginPath();
}

colorPicker.addEventListener("input", (event) => {
  selectedColor = event.target.value;
});

eraseButton.addEventListener("click", () => {
  erasing = !erasing;
  if (erasing) {
    eraseButton.textContent = "그리기";
  } else {
    eraseButton.textContent = "지우개";
  }
});

clearButton.addEventListener("click", () => {
  context.clearRect(0, 0, canvas.width, canvas.height);
});

storyButton.addEventListener("click", () => {
  const image = canvas.toDataURL("image/png");
  const link = document.createElement("a");
  link.href = image;
  link.download = "story.png";
  link.click();
});
