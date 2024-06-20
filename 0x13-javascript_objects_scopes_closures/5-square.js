#!/usr/bin/node
//defines a class Rectangular
const Rectangle = require('./4-rectangle');
module.exports = class square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
};