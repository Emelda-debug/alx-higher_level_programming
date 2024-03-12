#!/usr/bin/node
const files = require('files');
const file1Arg = files.readFileSync(process.argv[2]).toString();
const file2Arg = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], file1Arg + file2Arg);
