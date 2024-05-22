#!/usr/bin/node

const request = require('request');
// Note: function() inside the request should have 3 args (mandatory)
// err , res, body
request(process.argv[2], function(err, res, body) {
  console.log('code: ', res.statusCode)
});
