#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof this.cnt === 'undefined') {
    this.cnt = 0;
  }
  console.log(`${this.cnt}: ${item}`);
  this.cnt++;
};
