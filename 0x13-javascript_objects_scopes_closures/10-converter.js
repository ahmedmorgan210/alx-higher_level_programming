#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    const digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    let result = '';
    while (num > 0) {
      result = digits[num % base] + result;
      num = Math.floor(num / base);
    }
    return result;
  };
};
