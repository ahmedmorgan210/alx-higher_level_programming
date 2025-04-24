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

    double() {
        this.width = this.width * 2
        this.height = this.height * 2
        // for (let i = 0; i < this.height * 2; i++) {
        //     let output = '';
        //     for (let j = 0; j < this.width * 2; j++) {
        //         output += 'X';
        //     }
        //     console.log(output);
        // }
        
    }

    rotate() {

        [this.width , this.height] = [this.height, this.width];
        // for (let i = 0; i < this.height; i++) {
        //     let output = '';
        //     for (let j = 0; j < this.width; j++) {
        //       output += 'X';
        //     }
        //     console.log(output);
        // }
    }


}

module.exports = Rectangle;