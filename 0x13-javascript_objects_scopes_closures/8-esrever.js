#!/usr/bin/node

exports.esrever = function (list) {
  const revLst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revLst.push(list[i]);
  }
  return revLst;
};
