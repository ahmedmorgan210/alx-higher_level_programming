#!/usr/bin/node

const request = require('request');
// const episodeNum = 18;
// const apiUrl = process.argv[2];

const options = {
    url: 'https://swapi-api.alx-tools.com/api/films/' + '18',
    json: true
};

request(options, function(err, response, body) {
  if (err) {
    console.error('Request failed with status code:',err);
  } else if (response.statusCode == 200) {
    console.log(body);
  }
  
});