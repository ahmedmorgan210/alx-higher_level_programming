#!/usr/bin/node

function largest (array) {
  const argList = process.argv.slice(2);
  const argNum = argList.map(Number);

  if (argList.length < 2) {
    //console.log(0);
    return (0);
  } 
  if (!argNum) {
    //console.log(0);
    return (0);
  } else if (argNum) {
    argNum.sort((a, b) => b - a);

    const secondLargest = argNum[1];

    return (secondLargest);
  }
}
const secondLargestNumber = largest(process.argv);
console.log(secondLargestNumber);
