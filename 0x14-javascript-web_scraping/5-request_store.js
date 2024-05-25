#!/usr/bin/node

const fs = require('fs').promises; // Use fs.promises for asynchronous file operations
const request = require('request');

function writeFileFromUrl (url, filePath) {
  return new Promise((resolve, reject) => {
    request({ url, json: true }, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(new Error(`Failed to fetch data: ${error ? error.message : 'Unknown error'}`));
      } else {
        resolve(body);
      }
    });
  }).then(async (body) => {
    try {
      await fs.writeFile(filePath, JSON.stringify(body));
      console.log('Success: File written.');
    } catch (writeError) {
      console.error('Error writing to file:', writeError.message);
    }
  }).catch((fetchError) => {
    console.error('Fetch error:', fetchError.message);
  });
}

// Check if arguments are provided
if (process.argv.length > 3) {
  const url = process.argv[2];
  const filePath = process.argv[3];
  writeFileFromUrl(url, filePath);
} else {
  console.log('Usage: node script.js <URL> <file_path>');
}
