#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

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
