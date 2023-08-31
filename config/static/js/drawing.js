document.addEventListener("DOMContentLoaded", function () {
  const imageUpload = document.getElementById("imageUpload formFile");
  const canvas = document.getElementById("drawingCanvas");
  const context = canvas.getContext("2d");
  const colorPicker = document.getElementById("colorPicker");
  const eraseButton = document.getElementById("eraseButton");
  const clearButton = document.getElementById("clearButton");
  const storyButton = document.getElementById("storyButton");

  let isDrawing = false;

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

  function startDrawing(event) {
    isDrawing = true;
    draw(event);
  }

  function stopDrawing() {
    isDrawing = false;
    context.beginPath();
  }

  function draw(event) {
    if (!isDrawing) return;

    const color = colorPicker.value;
    context.lineWidth = 2;
    context.lineCap = "round";
    context.strokeStyle = color;

    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    const canvasX = (event.clientX - rect.left) * scaleX;
    const canvasY = (event.clientY - rect.top) * scaleY;

    context.lineTo(canvasX, canvasY);
    context.stroke();
    context.beginPath();
    context.moveTo(canvasX, canvasY);
  }

  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mousedown", startDrawing);
  canvas.addEventListener("mouseup", stopDrawing);
  canvas.addEventListener("mouseout", stopDrawing);

  eraseButton.addEventListener("click", function () {
    colorPicker.value = "#ffffff"; // 색상을 배경색으로 설정하여 지우개 역할
  });

  clearButton.addEventListener("click", function () {
    context.clearRect(0, 0, canvas.width, canvas.height);
  });

  // storyButton.addEventListener("click", () => {
  //   const image = canvas.toDataURL("image/png");
  //   const link = document.createElement("a");
  //   link.href = image;
  //   link.download = "story.png";
  //   link.click();
  // });
});
