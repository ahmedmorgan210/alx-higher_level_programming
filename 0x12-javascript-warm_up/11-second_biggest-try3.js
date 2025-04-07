#!/usr/bin/node

function largest (array) {
  // start the argument passed to the unction from the third arg
  // to exclude the process.argv[0] which is the path to the Node.js executable
  // and the process.argv[1] which is the path to the script file
  // process.argv[2] onwards are the arguments passed to the script.
  const argList = process.argv.slice(2);

  // Convert all arguments of the argument list from strings to numbers
  // using the .map method
  const argNum = argList.map(Number);

  if (argList.length < 2) {
    return (0);
  }

  if (!argNum) {
    return (0);
  } else if (argNum) {
    // Sort the list in descending order using .sort method
    argNum.sort((a, b) => b - a);

    const secondLargest = argNum[1];

    return (secondLargest);
  }
}
const secondLargestNumber = largest(process.argv);
console.log(secondLargestNumber);
