#!/usr/bin/node
// defines a class Rectangular
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const listKey in list) {
    if (list[listKey] === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
