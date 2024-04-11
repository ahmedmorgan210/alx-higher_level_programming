#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // this =
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

// In Node.js, to make a class or any other module available to other files, you need to export it using module.exports.

module.exports = Rectangle;
