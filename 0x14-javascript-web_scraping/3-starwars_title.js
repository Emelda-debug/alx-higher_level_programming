#!/usr/bin/node
const request = require('request');
// Constructing the URL for the Star Wars film
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Using the 'request' module for HTTP GET request to the aforementioned URL
request(url, function (error, response, body) {
  // If successful log title, else log error
  console.log(error || JSON.parse(body).title);
});
