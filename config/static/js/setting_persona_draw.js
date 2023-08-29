document.addEventListener("DOMContentLoaded", function () {
  const canvas = document.getElementById("characterCanvas");
  const context = canvas.getContext("2d");
  const colorPicker = document.getElementById("colorPicker");
  const eraseButton = document.getElementById("eraseButton");
  const clearButton = document.getElementById("clearButton");

  let isDrawing = false;

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
    context.lineWidth = 4;
    context.lineCap = "round";
    context.strokeStyle = color;

    context.lineTo(
      event.clientX - canvas.offsetLeft,
      event.clientY - canvas.offsetTop
    );
    context.stroke();
    context.beginPath();
    context.moveTo(
      event.clientX - canvas.offsetLeft,
      event.clientY - canvas.offsetTop
    );
  }

  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mousedown", startDrawing);
  canvas.addEventListener("mouseup", stopDrawing);
  canvas.addEventListener("mouseout", stopDrawing);

document.getElementById("saveButton").addEventListener("click", function() {
    window.location.href = "chatting";
});

  // const saveButton = document.getElementById("saveButton");
  // saveButton.addEventListener("click", function () {
  //   const characterName = document.getElementById("characterName").value;
  //   const ageSelect = document.getElementById("ageSelect").value;
  //   const genderSelect = document.getElementById("genderSelect").value;
  //   const likes = document.getElementById("likes").value;
  //   const dislikes = document.getElementById("dislikes").value;

  //   const characterData = {
  //     name: characterName,
  //     age: ageSelect,
  //     gender: genderSelect,
  //     likes: likes,
  //     dislikes: dislikes,
  //   };

  //   const dataString = JSON.stringify(characterData);
  //   const blob = new Blob([dataString], { type: "text/plain;charset=utf-8" });

  //   const downloadLink = document.createElement("a");
  //   downloadLink.href = URL.createObjectURL(blob);
  //   downloadLink.download = "character_data.txt";
  //   downloadLink.click();

  //   const canvasImage = canvas.toDataURL("image/png");
  //   const imageLink = document.createElement("a");
  //   imageLink.href = canvasImage;
  //   imageLink.download = "character_image.png";
  //   imageLink.click();
  // });

  eraseButton.addEventListener("click", function () {
    colorPicker.value = "#ffffff"; // 색상을 배경색으로 설정하여 지우개 역할
  });

  clearButton.addEventListener("click", function () {
    context.clearRect(0, 0, canvas.width, canvas.height);
  });
});
