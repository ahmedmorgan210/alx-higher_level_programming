#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let repete = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      repete += 1;
    }
  }
  return repete;
};
