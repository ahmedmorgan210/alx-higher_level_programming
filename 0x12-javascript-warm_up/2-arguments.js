#!/usr/bin/node
const args = process.argv;
const lens = args.length;

if (lens === 2) {
  console.log('No argument');
} else if (lens === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
