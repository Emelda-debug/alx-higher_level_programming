#!/usr/bin/node
let ArgNum = 0;
exports.logMe = function (item) {
  console.log(ArgNum + ':' + item);
  ArgNum++;
};
