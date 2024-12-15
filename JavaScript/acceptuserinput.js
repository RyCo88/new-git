//  How to accept user input

// 1. Easy way = window prompt

/*
let username; //let username = window.prompt();
 
username = window.prompt("What's your username? ");

console.log(username);
*/

// 2. Professional way = HTML textbox

let username;

document.getElementById("mySubmit").onclick = function(){
    username = document.getElementById("myText").value;
    //console.log(username);
    document.getElementById("myH1").textContent = `Hello ${username}`;
}