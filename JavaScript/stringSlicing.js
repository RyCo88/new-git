// string slicing =  creating a substring from a portion of another string
//                  string.slice(start, end)

const fullName = "Ryan Corson";

//let firstName = fullName.slice(0, 4); // the end point goes up to but does not include
//let lastName = fullName.slice(5, 11); //tuple could also be written as (5)

//let firstChar = fullName.slice(0, 1);
//let lastChar = fullName.slice(-1);

//console.log(firstName);
//console.log(lastName);
//console.log(firstChar);
//console.log(lastChar);

let firstName = fullName.slice(0, fullName.indexOf(' '));
let lastName = fullName.slice(fullName.indexOf(' ') +1);

console.log(firstName);
console.log(lastName);

const email = 'ryanconqueso@gmail.com';

let username = email.slice(0, email.indexOf("@"));
let extension = email.slice(email.indexOf("@") + 1);

console.log(username);
console.log(extension);