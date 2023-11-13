#!/usr/bin/node
// Write a script that prints the addition of 2 integers
// Function to compute the product of p1 and p2
function factorial (a) {
    let MyVar = 1;
    for (let i = 1; i <= parseInt(process.argv[2]); i++) {
      MyVar *= i;
    }
    return MyVar;
  }
  console.log(factorial(parseInt(process.argv[2])));
