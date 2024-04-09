#!/usr/bin/node

const toNumber = process.argv[2];
if (Number(toNumber)) {
  console.log(`My number: ${toNumber}`);
} else {
  console.log('Not a number');
}
