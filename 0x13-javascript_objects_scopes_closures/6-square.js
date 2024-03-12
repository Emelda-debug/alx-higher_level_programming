#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.height; j++) {
        rec += c;
      }
      console.log(rec);
    }
  }
}
module.exports = Square;
