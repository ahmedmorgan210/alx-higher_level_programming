#!/usr/bin/node

const fs = require('fs').promises;
const request = require('request');

async function writingFile(urlToText, filePath) {
  try {
    request(urlToText, { json: true }, function (err, response, body) {
      if (err ||!response || response.statusCode!== 200) {
        console.error('Error fetching data:', err || 'Request failed');
        return;
      }

      if (body && Object.keys(body).length!== 0) {
        fs.writeFile(filePath, JSON.stringify(body)).then(() => {
          console.log('Data written successfully.');
        }).catch((writeErr) => {
          console.error('Error writing file:', writeErr);
        });
      } else {
        console.log('No data received or data is empty.');
      }
    });
  } catch (error) {
    console.error(error);
  }
}

if (process.argv[3]) {
  writingFile(process.argv[2], process.argv[3]);
} else {
  console.log('');
}
