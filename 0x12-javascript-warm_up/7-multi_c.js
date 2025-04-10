#!/usr/bin/node

const { argv } = require('node:process');

if (!argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < argv[2]; x++) {
    console.log('C is fun');
  }
}
