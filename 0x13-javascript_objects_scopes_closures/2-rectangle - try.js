#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      // empty instance incase if no h or w passed
    } else if (w <= 0 || h <= 0) {
      // empty instance if w or h <= 0
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

// In Node.js, to make a class or any other module available to other files, you need to export it using module.exports.

module.exports = Rectangle;
