#!/usr/bin/node
exports.esrever = function (list) {
    const NewList = [];
    for (let i = 0; i < list.length; i++) {
      NewList.unshift(list[i]);
    }
    return NewList;
  };
