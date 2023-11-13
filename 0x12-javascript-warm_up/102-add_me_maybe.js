#!/usr/bin/node
// Write a function that executes x times a function.
exports.addMeMaybe = function (number, theFunction) {
    number += 1;
    theFunction(number);
  };