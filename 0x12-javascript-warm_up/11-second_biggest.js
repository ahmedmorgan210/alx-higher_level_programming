#!/usr/bin/node

const argList = process.argv.slice(2);
const argNum = argList.map(Number);

if (argList.length < 2) {
  console.log(0);
  return;
}

if (!argNum) {
  console.log(0);
} else if (argNum) {
  argNum.sort((a, b) => b - a);

  const secondLargest = argNum[1];

  console.log(secondLargest);
}
