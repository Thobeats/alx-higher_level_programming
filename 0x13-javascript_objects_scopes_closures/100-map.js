#!/usr/bin/node

const list = require('./100-data');
const list2 = list.map((lt, index)=>{
  return lt * index;
});

console.log(list);
console.log(list2);
