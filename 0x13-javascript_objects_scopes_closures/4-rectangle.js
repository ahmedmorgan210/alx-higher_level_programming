#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || h <= 0 || !h) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let output2 = '';
      for (let y = 0; y < this.width; y++) {
        output2 += 'X';
      }
      console.log(output2);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    // swap values of height and width using unpacking / Destructuring in JS
    // Resource:
    //      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
