#!/usr/bin/node
// Importing the 'request' module
const request = require('request');

request(process.argv[2], function (error, response, body) {
  // Check for errors during the HTTP request
  if (!error) {
    // parse the JSON data and extract the "results" array
    const results = JSON.parse(body).results;
    // The'reduce()' method is used to iterate through the movies in the 'results' array
    console.log(results.reduce((count, movie) => {
      // checking for a character with ID 18
      return movie.characters.find((character) => character.endsWith('/18/'))
        // If a character with ID 18 is found, increment count by 1.
        ? count + 1
        // Otherwise, keep count unchanged.
        : count;
      // 'reduce()' method starts with an initial value of 0 ('0' at the end).
    }, 0));
  }
});
