#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  const sum = a + b;
  return sum;
}
const firstNum = Number(argv[2]);
const secondNumber = Number(argv[3]);

if (!firstNum || !secondNumber) {
  console.log(NaN);
} else {
  const addition = add(firstNum, secondNumber);
  console.log(`${addition}`);
}
