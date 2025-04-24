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
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += 'X';
      }
      console.log(output);
    }
  }

  rotate () {
    const swappedWidth = this.height;
    const swappedHeight = this.width;
    for (let i = 0; i < swappedHeight; i++) {
      let output = '';
      for (let j = 0; j < swappedWidth; j++) {
        output += 'X';
      }
      console.log(output);
    }
  }

  double () {
    const dobleWidth = this.width * 2;
    const dobleHeight = this.height * 2;
    for (let i = 0; i < dobleHeight; i++) {
      let output = '';
      for (let j = 0; j < dobleWidth; j++) {
        output += 'X';
      }
      console.log(output);
    }
  }
}

module.exports = Rectangle;
