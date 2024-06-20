#!/usr/bin/node
// defines a class Rectangular
const squareModel = require('./5-square');
module.exports = class Square extends squareModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }
};
