#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/:id'; // Example ID

request(url, function(err, res, body) {
  if (err) {
    return console.log(err);
  }

  console.log('Status Code:', res.statusCode); // Debugging: Log the status code

  const filmId = parseInt(process.argv[2], 10);
  try {
    const parsedBody = JSON.parse(body);
    console.log('Parsed Body:', parsedBody); // Debugging: Log the parsed body
    if (parsedBody && parsedBody.id === filmId) {
      console.log(parsedBody.title);
    } else {
      console.log(`Film not found with ID ${filmId}`);
    }
  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});