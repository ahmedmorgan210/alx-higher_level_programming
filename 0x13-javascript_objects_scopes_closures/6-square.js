#!/usr/bin/node

const Ex = require('./5-square');

class Square extends Ex {
  // constructor (size) {
  //   super(size);
  // }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        let row = '';
        for (let y = 0; y < this.width; y++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

// In Node.js, to make a class or any other module available to other files, you need to export it using module.exports.

module.exports = Square;
