// for loop = repeat some code a LIMITED amount of times

/*
for(let i = 10; i > 0; i--){
    console.log(i);
}

console.log("HAPPY NEW YEAR!");
*/

/*
for(i = 1; i <= 20; i++){
    if(i == 13){
        continue;
    }
    else{
        console.log(i);
    }
}
*/

for(i = 1; i <= 20; i++){
    if(i == 13){
        break;
    }
    else{
        console.log(i);
    }
}