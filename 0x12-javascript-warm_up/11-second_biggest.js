#!/usr/bin/node

const { argv } = require('node:process');

// Resource in the below link
// https://www.w3schools.com/jsref/jsref_sort.asp

if (argv.length < 4) {
  console.log('0');
} else {
  const items = argv.slice(2);
  items.sort((a, b) => a - b);
  items.reverse();
  console.log(items[1]);
}
