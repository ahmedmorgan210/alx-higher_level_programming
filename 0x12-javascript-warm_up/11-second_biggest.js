#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 4) {
  console.log('0');
} else {
  const items = argv.slice(2);
  items.sort();
//   items.reverse();
  console.log(items[1]);
}
