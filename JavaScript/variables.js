/* 
variable = A container that stores a value
            behaves as if it were the value it contains

1. declaration      letx;
2. assignment       x = 100;
*/


/*
let x;
x = 123; // declaration and assignment would be let x = 123;

console.log(x);

let age = 25;
let price = 10.99;
let gpa = 2.1;

let firstName = "Bro";
let favoriteFood = "pizza";
let email = "Bro@gmale.com";

console.log(age);
console.log(price);
console.log(gpa);

console.log(typeof age);
console.log(typeof firstName);

console.log(firstName);
console.log(`Your name is ${firstName}`);
console.log(`You like ${favoriteFood}`);
console.log(`Your email is ${email}`);
console.log(`You are ${age} years old`);
console.log(`The price is $${price}`);
console.log(`Your gpa is ${gpa}`);

let online = true;
let forSale = true;
let isStudent = false;

console.log(typeof online);
console.log(`Bro is online: ${online}`);
console.log(`Is this car for sale: ${forSale}`);
console.log(`Enrolled: ${isStudent}`);
*/

let fullName = "Ryan Con Queso";
let age = 36;
let isStudent = false;

document.getElementById("p1").textContent = `Your name is ${fullName}`;
document.getElementById("p2").textContent = `You are ${age}`;
document.getElementById("p3").textContent = `Enrolled: ${isStudent}`;

