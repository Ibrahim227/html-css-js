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
const person = {
  fname: 'Mike',
  lname: 'Lawson',
  age: 46,
  eyeColor: 'Blue',
  jobStatus: 'Military',
  country: 'illinois',
  citizenship: 'USA',
  life: {
    currently: 'Jobless',
    ownCar: 'No',
    bankAccount: 'Bankrupt',
    children: 2
  }
};
document.getElementById("demo0").innerHTML = JSON.stringify(person);

let text = " ";
for (let x in person) {
  text += person[x] + " ";
}
document.getElementById("demo1").innerHTML = JSON.stringify(text);

const myArray = Object.values(person);

document.getElementById("demo2").innerHTML = JSON.stringify(myArray);

const fruits = {Bananas:300, Oranges:200, Apples:500};

const txt = "";

for (let [fruit, value] of Object.entries(fruits)) {
  txt += fruit + ": " + value + '<br>';
}
document.getElementById("demo3").innerHTML = JSON.stringify(txt);

function displayTime() {
  time = Date();
  this.innerHTML = time;
};
document.getElementById("demo4").innerHTML = displayTime();
