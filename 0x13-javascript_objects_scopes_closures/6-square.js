#!/usr/bin/node

const parentSquare = require('./5-square.js');

class Square extends parentSquare {
  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.height; x++) {
        let output = '';
        for (let y = 0; y < this.width; y++) {
          output += 'C';
        }
        console.log(output);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
