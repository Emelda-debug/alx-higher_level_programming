#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  let x = 0;
  while ((l - x > 0)) {
    const rev = list[l];
    list[l] = list[x];
    list[x] = rev;
    x++;
    l--;
  }
  return list;
};
