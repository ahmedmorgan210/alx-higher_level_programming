#!/usr/bin/node

const mainDict = require('./101-data').dict;

const newDict = {};

for (const userId in mainDict) {
  const occurrence = mainDict[userId];
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userId);
}

console.log(newDict);
