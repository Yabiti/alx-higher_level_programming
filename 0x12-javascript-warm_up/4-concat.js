#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed
if (process.argv.slice(2).length < 1) {
    console.log('undefined is undefined');
  } else if (process.argv.slice(2).length === 1) {
    console.log(process.argv[2] + ' is undefined');
  } else {
    console.log(process.argv[2] + ' is ' + process.argv[3]);
  }