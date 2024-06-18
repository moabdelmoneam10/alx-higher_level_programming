#!/usr/bin/node
// Script that prints a square
const len = process.argv[2];

if (!parseInt(len)) console.log('Missing size');
for (let i = 0; i < len; i++) {
  console.log('X'.repeat(len));
}
