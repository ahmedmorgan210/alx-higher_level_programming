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

  print () {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

// In Node.js, to make a class or any other module available to other files, you need to export it using module.exports.

module.exports = Rectangle;
