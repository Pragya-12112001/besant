
function changeColor() {
  let color = document.getElementById("color").value.trim();

  if (CSS.supports("color", color)) {
    document.body.style.backgroundColor = color;
  } else {
    alert("Enter a valid color");
  }
}

function greet() {
  let name = document.getElementById("name").value.trim();
  document.getElementById("greeting").innerText = `Hello ${name}`;
}

function changeHeading() {
  let text = document.getElementById("headingInput").value;
  document.getElementById("heading").innerText = text;
}

function changeFontSize() {
  let size = Number(document.getElementById("fontSize").value);

  if (size > 0) {
    document.getElementById("text").style.fontSize = size + "px";
  }
}

function changeBoxColor() {
  let color = document.getElementById("boxColor").value.trim();

  if (CSS.supports("color", color)) {
    document.getElementById("box").style.backgroundColor = color;
  } else {
    alert("Enter a valid color");
  }
}

function calculateSquare() {
  let value = document.getElementById("squareInput").value;

  if (value.trim() === "") {
    document.getElementById("squareResult").innerText =
      "Please enter a number";
    return;
  }

  let num = Number(value);
  document.getElementById("squareResult").innerText =
    `Square: ${num * num}`;
}

function joinNames() {
  let first = document.getElementById("firstName").value.trim();
  let last = document.getElementById("lastName").value.trim();

  document.getElementById("fullName").innerText =
    `${first} ${last}`.trim();
}

function addItem() {
  let value = document.getElementById("itemInput").value.trim();

  if (value === "") {
    alert("Enter an item");
    return;
  }

  let li = document.createElement("li");
  li.innerText = value;
  document.getElementById("list").appendChild(li);
}

function changeWidth() {
  let width = Number(document.getElementById("widthInput").value);

  if (width > 0 && width <= 1000) {
    document.getElementById("widthBox").style.width = width + "px";
  }
}

function removeElement() {
  let id = document.getElementById("elementId").value.trim();
  let element = document.getElementById(id);

  if (element && id !== "removeResult") {
    element.remove();
    document.getElementById("removeResult").innerText = "Element removed";
  } else {
    document.getElementById("removeResult").innerText =
      "Element not found or cannot be removed";
  }
}
