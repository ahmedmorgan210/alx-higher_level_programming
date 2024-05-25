#!/usr/bin/node

const fs = require('fs').promises;
const request = require('request');

let data; // Declare the variable outside the function

async function fetchDataAndWriteToFile(url, filePath) {
  try {
    const response = await new Promise((resolve, reject) => {
      request(url, { json: true }, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          resolve(body); // Resolve the promise with the body
        } else {
          reject(new Error(`Request failed with status ${response? response.statusCode : 'unknown'} ${body}`));
        }
      });
    });

    data = response; // Update the global variable with the fetched data

    await fs.writeFile(filePath, JSON.stringify(response));
    console.log('Data written successfully');
  } catch (error) {
    console.error(error);
  }
}

fetchDataAndWriteToFile(process.argv[2], process.argv[3]);

console.log(data); // Access the updated data variable