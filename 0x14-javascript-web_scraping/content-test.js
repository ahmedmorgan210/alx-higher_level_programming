#!/usr/bin/node

const request = require('request');

// Specify the episode ID you're interested in
const episodeId = 4; // Example ID, replace with the actual ID you want to search for

request('https://swapi-api.alx-tools.com/api/films/', function(err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log('Response Status Code:', res.statusCode);
  
  let parsedBody;
  try {
    parsedBody = JSON.parse(body);
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  // Check if parsedBody and parsedBody.results exist before proceeding
  if (!parsedBody ||!parsedBody.results) {
    console.log('Data not available or incorrectly structured.');
    return;
  }

  // Find the film with the specified episode ID
  const film = parsedBody.results.find(film => film.episode_id === episodeId);

  if (film) {
    console.log('Title of Episode with ID', episodeId, ':', film.title);
  } else {
    console.log(`No film found with episode ID ${episodeId}`);
  }
});
