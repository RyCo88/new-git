// string methods = allow you to manipulate and work with text (strings)

let userName = "RyanCon Queso";

console.log(userName.charAt(0)); //charAt method returns character at specified index

console.log(userName.indexOf('o')); // returns index of first occurrence of the specified element/character

console.log(userName.lastIndexOf('o')); // returns the last index of specified character

console.log(userName.length); //returns the length of the element 

userName = userName.trim(); //trims any whitespace in the code

console.log(userName);

console.log(userName.toUpperCase()); //return variable in upper case

console.log(userName.toLowerCase()); //return variable in lowercase

console.log(userName.repeat(3)); //repeat the variable the specified number of times

console.log(userName.startsWith('R')); //will check and return a boolean function

/*let result = userName.startsWith(''); // will return a boolean to assess if true or false

if(result){
    console.log("Your username can't begin with a ' '")
}
else{
    console.log(userName)
}

let result = userName.endsWith(''); // will return a boolean to assess if true or false

if(result){
    console.log("Your username can't end with a ' '")
}
else{
    console.log(userName)
}

let result = userName.includes(" ");

if(result){
    console.log("Your username can't include a ' '");
}
else{
    console.log(userName);
}

let phoneNumber = "123-456-7890";

phoneNumber = phoneNumber.replaceAll("-", "/") //replace characters. Use the first argument to discern which characters to replace, use the second to what the first character will be replaced with
console.log(phoneNumber)

let phoneNumber = "123-456-7890";

phoneNumber = phoneNumber.padStart(15, "/"); //set a length value to set how long you want the string variable to be, use the 2nd value to fill unused spots in with the specified character
console.log(phoneNumber); */

let phoneNumber = "123-456-7890";

phoneNumber = phoneNumber.padEnd(15, "/"); //set a length value to set how long you want the string variable to be, use the 2nd value to fill unused spots in with the specified character
console.log(phoneNumber);