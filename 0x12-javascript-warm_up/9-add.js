#!/usr/bin/node

function add(a, b) {
  let addition = a + b;
  console.log(addition);
}

arg1 = parseInt(process.argv[2]);
arg2 = parseInt(process.argv[3]);
add(arg1, arg2);
