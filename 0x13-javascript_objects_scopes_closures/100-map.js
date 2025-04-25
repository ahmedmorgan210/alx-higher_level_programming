#!/usr/bin/node

const { list } = require('./100-data');

const map = require('./100-data').list;

const newList = list.map((value, index) => {
  return value * index;
});

console.log(newList);
