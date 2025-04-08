#!/usr/bin/node
const { argv } = require('node:process');
// const argv = process.argv;
// const convertedNumber = Math.floor(Number(argv[2]));

const convertedNumber = Number(argv[2]);

if (!convertedNumber) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
