#!/usr/bin/node

function add(a, b) {
  let addition = a + b;
  return addition;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
console.log(add(arg1, arg2));
