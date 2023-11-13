#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed
if (process.argv.slice(2).length < 1) {
    console.log('No argument');
  } else if (process.argv.slice(2).length === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }