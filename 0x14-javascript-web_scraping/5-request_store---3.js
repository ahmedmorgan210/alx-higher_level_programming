#!/usr/bin/node

const fs = require('fs').promises;
const request = require('request');

async function writingToFile (contentUrl, filePath) {
  try {
    let data = '';

    await fs.writeFile(filePath, data);
    request(contentUrl, { json: true }, function (err, res, body) {
      if (!err && res.statusCode === 200) {
        data += body;
      }
    });

    // await fs.writeFile(filePath, data);
    console.log('Data written successfully');
  } catch (error) {
    console.error(error);
  }
}

writingToFile(process.argv[2], process.argv[3]);
