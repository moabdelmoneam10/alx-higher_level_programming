#!/usr/bin/node
// defines a class Rectangular
const SquareModel  = require('./5-square');
module.exports = class Square extends SquareModel  {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }
};
