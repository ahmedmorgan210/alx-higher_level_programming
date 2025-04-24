#!/usr/bin/node

exports.esrever = function (list) {
  for (let x = 0; x < Math.floor(list.length / 2); x++) {
    const temp = list[x];
    list[x] = list[list.length - 1 - x];
    list[list.length - 1 - x] = temp;
  }
  return list;
};
