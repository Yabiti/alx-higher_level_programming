#!/usr/bin/node
// Write a script that prints a square
if (process.argv.slice(2).length < 1) {
    console.log('Missing size');
  } else if (parseInt(process.argv[2])) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      let MyVar = '';
      for (let i = 0; i < parseInt(process.argv[2]); i++) {
        MyVar += 'X';
      }
      console.log(MyVar);
    }
  } else {
    console.log('Missing size');
  }