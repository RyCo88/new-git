// function = A section of reusable code.
//              Declare a code once, use it whenever you want.
//              Call the function to exectute that code

/*
function happyBirthday(username, age){ //order of parameters matter
    console.log("Happy birthday to you!");
    console.log("Happy birthday to you!");
    console.log(`Happy birthday dear ${username}!`);
    console.log("Happy birthday to you!");
    console.log(`You are ${age} years old`);
}

happyBirthday("RyanConQueso", 36); //make sure parameters match up
happyBirthday('Spongebob', 30);
*/

/*
function add(x, y){
    let result = x + y;
    return result;
}

let answer = add(2,3);
console.log(answer);
*/

function add(x, y){ //without setting a variable
    return x + y;
}

console.log(add(2,3));

function subtract(x,y){
    return x-y;
}
console.log(subtract(2,3));

function multiply(x,y){
    return x*y;
}
console.log(multiply(2,3));

function divide(x,y){
    return x/y;
}
console.log(divide(2,3));

function isEven(num){
    if(num % 2 == 0){
        return true;
    }
    else{
        return false;
    }
}

/* written with Ternary Operator
function isEven(num){

    return number % 2 === 0 ? true : false;
}
*/
console.log(isEven(7));
console.log(isEven(10));

function isValidEmail(email){
    if(email.includes("@")){
        return true;
    }
    else{
        return false;
    }
}
/* written with Ternary Operator
function isValidEmail(email){

    return email.includes("@") ? true : false;
}
*/
console.log(isValidEmail("ryanconqueso@gmail.com"))
console.log(isValidEmail("ryanconqueso.com"))