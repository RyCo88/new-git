// array = a variable like structure that can hold more than 1 value

let fruits = ["apple", "orange", "banana"];

//fruits[3] = "coconut"; you can add an item this way
fruits.push("coconut"); // you can also add items this way
//fruits.pop(); //remove the last element
fruits.unshift('mango'); //adds item to the beginning of array
//fruits.shift(); //remove an element from the beginning

console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);
console.log(fruits[3]);
console.log(fruits[4]);

let numOfFruits = fruits.length;
let index = fruits.indexOf("apple"); //if an item doesn't exist it will return -1

console.log(numOfFruits);
console.log(index);

fruits.sort() //will sort items alphabetically for strings
fruits.sort().reverse() // will sort items in reverse order

for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}

for(let i = fruits.length -1; i >=0; i--){
    console.log(fruits[i]);
}
for (let fruit of fruits){
    console.log(fruit)
}