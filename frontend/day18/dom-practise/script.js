
/* Task 1: Change Text */
function task1() {
    let text = document.getElementById("text1");
    text.innerText = "Text Changed Successfully!";
}

/* Task 2: Change Text Color */
function task2() {
    let text = document.getElementById("text2");
    text.style.color = "red";
}

/* Task 3: Change Background Color */
function task3() {
    let text = document.getElementById("text3");
    text.style.backgroundColor = "yellow";
}

/* Task 4: Toggle Dark Mode */
let isDark = false;

function task4() {
    let btn = document.getElementById("mode");
    let text = document.getElementById("text4");

    if (isDark === false) {
        document.body.style.backgroundColor = "black";
        document.body.style.color = "white";
        btn.innerText = "Light";
        text.innerText = "Dark Mode";
        isDark = true;
    } else {
        document.body.style.backgroundColor = "white";
        document.body.style.color = "black";
        btn.innerText = "Dark";
        text.innerText = "Light Mode";
        isDark = false;
    }
}

/* Task 5: Show and Hide Text */
function task5() {
    let text = document.getElementById("text5");

    if (text.style.display === "none") {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
}

/* Task 6: Increase Font Size */
let fontSize = 18;

function task6() {
    let text = document.getElementById("text6");

    fontSize += 2;
    text.style.fontSize = fontSize + "px";
}

/* Task 7: Change Text and Color */
function task7() {
    let text = document.getElementById("text7");

    text.innerText = "Text and Color Changed!";
    text.style.color = "green";
}

/* Task 8: Toggle Red and Blue */
let isRed = false;

function task8() {
    let text = document.getElementById("text8");

    if (isRed === false) {
        text.style.color = "red";
        text.innerText = "I am Red!";
        isRed = true;
    } else {
        text.style.color = "blue";
        text.innerText = "I am Blue!";
        isRed = false;
    }
}

/* Task 9: Change Button Text */
function task9() {
    let btn = document.getElementById("btn9");
    let text = document.getElementById("text9");

    if (btn.innerText === "Click Me") {
        btn.innerText = "Clicked!";
        text.innerText = "Button text changed.";
    } else {
        btn.innerText = "Click Me";
        text.innerText = "Click the button below";
    }
}


/* Task 10: Toggle Uppercase and Lowercase */
function task10() {
    let text = document.getElementById("text10");

    if (text.style.textTransform !== "uppercase") {
        text.style.textTransform = "uppercase";
    } else {
        text.style.textTransform = "lowercase";
    }
}
