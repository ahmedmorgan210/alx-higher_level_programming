#!/usr/bin/node

const argList = process.argv.slice(2);

const sortedList = [];

if (argList.length < 4) {
  console.log(0);
  return;
}

// const y = 0;

for (let x = 0; x < 2; x++) {
  let y = 0;
  for (let j = argList[2]; j < argList.length; j++) {
    if (argList[j] >= argList[j + 1]) {
      y = Number(argList[j]);
    }
  }
  sortedList.push(y);
}
console.log(sortedList[1]);
