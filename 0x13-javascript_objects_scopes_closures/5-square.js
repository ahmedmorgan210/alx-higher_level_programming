#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

// In Node.js, to make a class or any other module available to other files, you need to export it using module.exports.

module.exports = Square;
