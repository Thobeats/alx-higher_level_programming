#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myX = '';
    let i = 0;
    while (i < this.height) {
      let j = 0;
      while (j < this.width) {
        myX += 'X';
        j++;
      }
      console.log(myX);
      i++;
    }
  }
}

module.exports = Rectangle;
