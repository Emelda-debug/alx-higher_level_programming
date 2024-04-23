#!/usr/bin/node

const fs = require('fs');
// Importing the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file specified as a command-line argument
  // 'utf8' specifies the encoding of the file being read

  if (error) {
    // If an error occurs during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error! can not read file:', error);
  } else {
    // If the file reading is successful, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
  }
});
