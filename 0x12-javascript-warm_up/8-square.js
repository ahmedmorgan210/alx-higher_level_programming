#!/usr/bin/node

const { argv } = require('node:process');

const size = Number(argv[2]);

if (!size) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    let square = '';
    for (let y = 0; y < size; y++) {
      square += 'X';
    }
    console.log(square);
  }
}
