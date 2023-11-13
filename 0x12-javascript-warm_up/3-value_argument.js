#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed
if (!process.argv[2]) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
} 