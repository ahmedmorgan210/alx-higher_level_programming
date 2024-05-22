#!/usr/bin/node
const fs = require('fs').promises;

async function readFile (filePath) {
  try {
    const data = await fs.readFile(filePath);
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}
readFile(process.argv[2]);

// try {
//   fs.readFile(process.argv[2]).then(data => {
//     // Once the promise resolves, convert the buffer to a string and log it
//     console.log(data.toString());
//   }).catch(error => {
//     // Handle any errors that occur during file reading
//     console.error(error);
//   });
// } catch (error) {
//   // Handle any other errors that might occur
//   console.error(error);
// }
