#!/usr/bin/node
const fs = require('fs');
// Importing the built-in Node.js 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Using fs.writeFile() to write data where first argument is the file path(process.argv[2]).
  // The data to be written is from the fourth command-line argument (process.argv[3]).

  if (error) {
    // If an error occurs, the 'error' parameter will contain an error object.
    console.error(error);
  }
});
