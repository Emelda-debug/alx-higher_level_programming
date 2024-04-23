#!/usr/bin/node
const request = require('request');
// Import the 'request' module.

request.get(process.argv[2])
// Using the 'request' module to perform an HTTP GET request to the URL

  .on('response', function (response) {
    // Setting up event listener for the 'response' from the HTTP request.

    console.log(`code: ${response.statusCode}`);
    // Logging the HTTP status code of the response to the console
  });
