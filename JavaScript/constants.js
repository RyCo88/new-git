// const = a variable that can't be changed

const PI = 3.14159; //strings are not typically capitalized with const, booleans and numbers are capitalized for best practice
let radius;
let circumference;

//radius = window.prompt("Enter the raius of a circle");
radius = Number(radius);

circumference = 2 * PI * radius;

//console.log(circumference);

document.getElementById("mySubmit").onclick = function(){
    radius = document.getElementById("myText").value;
    radius = Number(radius);
    circumference = 2 * PI * radius;
    document.getElementById("myH3").textContent = circumference + "cm";
}