#!/usr/bin/node
// defines a class Rectangular
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) { return; }
    this.width = w;
    this.height = h;
  }
};
