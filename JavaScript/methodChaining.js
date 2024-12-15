// Method Chaining = Calling one method after another in one continuous line of code.

// NO METHOD CHAINING
/*
// trim whitespace, capitalize first character, lowercase other characters, display output
let username = window.prompt("Enter your username: ");

username = username.trim(); //Trim whitespace
let letter = username.charAt(0); //store first character as variable
letter = letter.toUpperCase(); //make first character capitalized

let extraChars = username.slice(1); //grab rest of the username
extraChars = extraChars.toLowerCase(); //make the rest of username lowercase
username = letter + extraChars; //combine first letter and rest of characters together to return the username first letter Capitalized rest lowercase without whitespace

console.log(username);
*/

// METHOD CHAINING

let username = window.prompt("Enter your username: ");

username = username.trim().charAt(0).toUpperCase() + username.trim().slice(1).toLowerCase();
console.log(username);
