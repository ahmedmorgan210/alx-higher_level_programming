#!/usr/bin/node

const request = require('request');
// Notes: function() inside the request should have 3 args (mandatory)
//            err , res, body
// you have to handle a to handle the error case
request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log('code:', res.statusCode);
});
