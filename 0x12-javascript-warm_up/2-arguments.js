#!/usr/bin/node
const { argv } = require('node:process');

if ((argv.length - 2) === 0) {
  console.log('No argument');
} else if ((argv.length - 2) === 1) {
  console.log('Argument found');
} else if ((argv.length - 2) > 1) {
  console.log('Arguments found');
}
