// logical operators = used to combine or manipulate boolean values (true of false)
//                      AND = &&
//                      OR = ||
//                      NOT = !

const temp = 20;

/* THIS WON'T WORK
if(temp > 0){
    console.log("The weather is GOOD");
}
else if(temp <= 30){
    console.log("The weather is GOOD") ;   
}
else{
    console.log("The weather is BAD");
}*/


if(temp > 0 && temp <= 30){
    console.log("The weather is GOOD");
}
else{
    console.log("The weather is BAD");
}


if(temp <= 0 || temp > 30){
    console.log("The weather is BAD");
}
else{
    console.log("The weather is GOOD");
}

const isSunny = true;

if(isSunny){
    console.log("It is SUNNY");
}
else{
    console.log("It is CLOUDY");
}

if(!isSunny){
    console.log("It is CLOUDY");
}
else{
    console.log("It is SUNNY");
}