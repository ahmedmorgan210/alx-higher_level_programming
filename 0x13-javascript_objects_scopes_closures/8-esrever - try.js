#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];

  // convert "list" to array to be able to iterate over and to get its length
  // let arr = Array.from(list)
  for (let x = (list.length - 1); x >= 0; x--) {
    newList.push(list[x]);
  }
  return (newList);
};
