/*
arithmetic operators = operands (values, variables, etc.)
                        operators (+ - * /)
                        example: 11 = x + 5;

*/

let students = 30;

//students = students + 1; addition
//students = students - 1; subtraction
//students = students * 2; multiplication
//students = students / 2; division
//students = students ** 2; exponents
//students = students % 2; modulus, probably better to write a new variable for this answer

    //augmented assignment operators
//students += 1; quicker reassignment same for -= *= /= **= and %=

//students ++; increment operator, increases count by 1
//students --; decrement operator, decreases count by 1

console.log(students);

/*
    operator precedence
    1. parenthesis ()
    2. exponents
    3. multiplication & division & modulo
    4. addition & subtraction
*/

let result = 1 + 2 * 3 + 4 ** 2;

console.log(result);