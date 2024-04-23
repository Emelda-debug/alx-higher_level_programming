#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  // Check for errors during the HTTP request
  if (!error && response.statusCode === 200) {
    // Parsing the JSON response body
    const movieData = JSON.parse(body);
    // Creating an array of promises that fetch data for each character
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        // Using another 'request' to fetch data for the character
        request(characterUrl, function (charError, charResponse, charBody) {
          // Checking for errors during the HTTP request
          if (!charError && charResponse.statusCode === 200) {
            // Parsing the JSON response body
            const characterData = JSON.parse(charBody);
            // Resolving the promise with the character name
            resolve(characterData.name);
          } else {
            // Rejecting the promise with the error message if there was an error during the HTTP request
            reject(new Error(`Error! could not fetch character data: ${charError}`));
          }
        });
      });
    });

    // Handling the character promises
    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames);
      })
      .catch((error) => {
        console.error(error);
      });
  } else {
    console.error(`Error! could not fetch movie data: ${error}`);
  }
});
