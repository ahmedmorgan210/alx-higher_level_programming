#!/usr/bin/node

const number = Number(process.argv[2]);

if (number) {
  for (let x = 0; x < number; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
