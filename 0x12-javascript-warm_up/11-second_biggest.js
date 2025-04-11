#!/usr/bin/node

const { argv } = require('node:process');

// Resource in the below link
// https://www.w3schools.com/jsref/jsref_sort.asp

/*
The issue in your code is that JavaScript (and Node.js) doesn't support negative array indices in the same way some other languages like Python do.

When you do console.log(items[-2]), you're not accessing the second last element of the array - you're actually trying to access a property named "-2" of the array object, which doesn't exist (hence you get undefined).

In JavaScript, to get the second last element of an array, you should use the array's length property. Here's how you can fix it:
console.log(items[items.length - 2]);
This works because:

items.length gives you the total number of elements

We subtract 2 to get the second last index (since array indices are 0-based)

For example, if your array has 5 elements, items.length is 5, and items.length - 2 is 3, which would be the index of the second last element (since indices are 0, 1, 2, 3, 4).
*/

if (argv.length < 4) {
  console.log('0');
} else {
  const items = argv.slice(2);
  items.sort((a, b) => a - b);
  // console.log(items);
  // console.log(items[-2]);
  items.reverse();
  console.log(items[1]);
  // console.log(items.length - 2);
}
