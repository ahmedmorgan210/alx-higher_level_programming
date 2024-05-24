#!/usr/bin/node

const request = require('request');
// import request from 'request';
const episodeNum = '?ID=18&character=Wedge%20Antilles';
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
