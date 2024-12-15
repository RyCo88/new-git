// variable scope = where a variable is recognized and accessible (local vs global)

// you can not re-use variable names if they are in the same scope (global or local)
// you can re-use variable names if they are in different scopes
/*
function function1(){
    let x = 1; //variables within a function or curly braces is considered local scope
    console.log(x);
}

function function2(){
    let x = 2;
    console.log(x);
}
//functions can not see into other functions, so if the same variable name is used it won't be noticed

function1();
function2();
*/


// a global scope is any variable declared outside of a function

    //functions are like houses, we can see what's insid the house if we're in that function
    //global functions are outside of the function houses. The inside of the functions can see the global ones out of the windows
let x = 3;
let y = 4;

function function1(){
    //if there's a function that has a local variable of the same name as a global, they would reference the local variable, otherwise they would use the global
    console.log(x);
}

function function2(){
    console.log(y);
}

function1();
function2();