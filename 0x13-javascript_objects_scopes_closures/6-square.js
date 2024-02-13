#!/usr/bin/node
// class Square that defines a square and
// inherits from Square of 5-square.js

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charprint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
}
module.exports = Square;
