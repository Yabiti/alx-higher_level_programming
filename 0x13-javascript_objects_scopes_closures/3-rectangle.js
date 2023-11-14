#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle
module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        // If w and h are greater than 0
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      // nstance method called print() that prints the rectangle using the character X
      for (let i = 0; i < this.height; i++) {
        let MyVar = '';
        for (let j = 0; j < this.width; j++) {
          MyVar += 'X';
        }
        console.log(MyVar);
      }
    }
  };