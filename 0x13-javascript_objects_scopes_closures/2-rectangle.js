#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (x, y) {
    if (x > 0 && y > 0) {
      this.width = x;
      this.height = y;
    }
  }
}

module.exports = Rectangle;
