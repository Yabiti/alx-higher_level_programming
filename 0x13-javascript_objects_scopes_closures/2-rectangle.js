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
  };