#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        let MyVar = '';
        for (let j = 0; j < this.height; j++) {
          MyVar += c;
        }
        console.log(MyVar);
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        let MyVar = '';
        for (let j = 0; j < this.height; j++) {
          MyVar += 'X';
        }
        console.log(MyVar);
      }
    }
  }
};
