#!/usr/bin/node

const { title } = require('process');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function(error, response, body){

  let wedgeAntilles;

  if (!error && response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    for (title in responseJSON) {
      console.log(title);
    }
  }
});