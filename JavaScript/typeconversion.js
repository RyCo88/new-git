// type conversion = change the datatype of a value to another
//                      (strings, numbers, booleans)

/*
let age = window.prompt("How old are you?");

age = Number(age);
age+=1;

console.log(age, typeof age);
*/

let x = "pizza";
let y = "pizza";
let z = "pizza";

x = Number(x);
y = String(y);
z = Boolean(z);

console.log(x, typeof x); //will return NaN for Not a Number
console.log(y, typeof y);
console.log(z, typeof z); //booleans are true or false, if there is a value it will always be true unless it's a number 0 or an empty item