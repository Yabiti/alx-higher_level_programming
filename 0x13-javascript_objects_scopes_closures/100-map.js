#!/usr/bin/node
const Mylist = require('./100-data.js').list;
const NewList = Mylist.map((x, y) => x * y);
console.log(Mylist);
console.log(NewList);
