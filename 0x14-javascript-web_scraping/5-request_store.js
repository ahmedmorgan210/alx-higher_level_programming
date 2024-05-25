#!/usr/bin/node

const fs = require('fs').promises;
const request = require('request');

async function writingFile (urlToText, filePath) {
  // options = {
  //   url: urlToText,
  //   json: true
  // };
  try {

    request(urlToText, { json: true }, function (err, response, body) {
      if (!err && response.statusCode === 200) {
        // const responseJson = JSON.parse(body);

        // fs.writeFile(filePath, body);

        if (Object.keys(body).length != 0){
          fs.writeFile(filePath, body);
        }
        
        // if (Object.keys(body).length === 0){
        //   console.log('');
        // } else {
        //   fs.writeFile(filePath, body);
        // }

      } else {
        console.error(err);
      }
    });
  } catch (error) {
    console.error(error);
  }
}

if (process.argv[3]){
  writingFile(process.argv[2], process.argv[3]);
} else {
  console.log('');
}
