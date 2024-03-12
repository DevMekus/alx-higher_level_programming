#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let index = 0;

  while ((len - index) > 0) {
    const temp = list[len];
    list[len] = list[index];
    list[index] = temp;
    index++;
    len--;
  }
  return list;
};
