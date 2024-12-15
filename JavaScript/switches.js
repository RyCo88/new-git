// SWITCH = can be an effective replacement to many else if statements

/*let day = "pizza";

switch(day){
    case 1:
        console.log("It is Monday");
        break; //break statements are to break out of the switch if a case matches
        // in js if there is no break in the case then the code will cascade down the lines and return each case after the input variable
    case 2:
        console.log("It is Tuesday");
        break;
    case 3:
        console.log("It is Wednesday");
        break;
    case 4:
        console.log("It is Thursday");
        break;
    case 5:
        console.log("It is Friday");
        break;
    case 6:
        console.log("It is Saturday");
        break;
    case 7:
        console.log("It is Sunday");
        break;
    default: //set a default value for a response if a case is not matched
        console.log(`${day} is not a day`)     
}*/

let testScore = 33;
let letterGrade;

switch(true){
    case testScore >= 90:
        letterGrade = "A"
        break;
    case testScore >= 80:
        letterGrade = "B"
        break;
    case testScore >= 70:
        letterGrade = "C"
        break;
    case testScore >= 60:
        letterGrade = "D"
        break;
    default:
        letterGrade = "F"
}



console.log(letterGrade)