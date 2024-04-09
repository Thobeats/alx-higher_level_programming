#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c = 'X') {
    let myX = '';
    let i = 0;
    let j = 0;
    while (j < this.width) {
      myX += c;
      j++;
    }

    while (i < this.height) {
      console.log(myX);
      i++;
    }
  }
}

module.exports = Square;
