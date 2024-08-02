//console.log("logTerm");

function CoffeeClick () {
    alert("You will be redirected to the owner of the coffee shop!");
}

function myFunction() {
    var x = document.getElementsByClassName("note");
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
}

const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/regx.jpg") {
    myImage.setAttribute("src", "images/workplace.jpg");
  } else {
    myImage.setAttribute("src", "images/regx.jpg");
  }
};

function changeValue() {
    document.getElementById("pre-btn").innerHTML = "Javascript changed this content after the Click!";
    window.alert("Javascript changed this content after the Click!");
    console.log("Javascript changed this content after the Click!");
}