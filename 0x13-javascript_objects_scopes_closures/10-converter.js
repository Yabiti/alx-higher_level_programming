#!/usr/bin/node
exports.converter = function (base) {
    function myconverter (number) {
      return number.toString(base);
    }
    return myconverter;
  };