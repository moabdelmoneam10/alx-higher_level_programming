#!/usr/bin/node
// Script that prints "C is fun" x times
const args = process.argv[2];

if (args === undefined) {
  console.log('Missing number of occurences');
}
for (let index = 0; index < args; index++) {
  console.log('C is fun');
}
