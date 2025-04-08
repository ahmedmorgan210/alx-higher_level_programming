#!/usr/bin/node
const { argv } = require('node:process');

// const args = process.argv.slice(2);

// https://nodejs.org/api/process.html#process_process_argv       # How to handle arguments passed to the script seams like argc and argv in C language

if (argv[2] == null) {
  console.log('No argument');
} else {
  // remove the first 2 elements passed to get the actual argumet passed
  // https://stackoverflow.com/questions/50359735/how-do-i-make-process-argv-print-only-the-arguments-and-not-the-path-or-node-co
  // const args = process.argv.slice(2);
//   console.log(args[0]);
  console.log(argv[2]);
}
