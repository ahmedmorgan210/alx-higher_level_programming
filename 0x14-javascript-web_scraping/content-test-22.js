#!/usr/bin/node


const request = require('request');


const episodeId = 4;
// Notes: function() inside the request should have 3 args (mandatory)
//            err , res, body
// you have to handle a to handle the error case

request('https://swapi-api.alx-tools.com/api/films/:id', function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log('code:', res.statusCode);
  let parseBody;

  try {
    parseBody = JSON.parse(body);
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  // Find the film with the specified episode ID
  const film = parseBody.results.find(film => film.episode_id === episodeId);

  if (film) {
    console.log('Title of Episode with ID', episodeId, ':', film.title);
  } else {
    console.log(`No film found with episode ID ${episodeId}`);
  }
});
