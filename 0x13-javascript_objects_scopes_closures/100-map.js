#!/usr/bin/node

const { list } = require('./100-data');

const map1 = require('./100-data').list;

const newList = list.map((value, index) => {
  return value * index;
});
console.log(map1)
console.log(newList);
