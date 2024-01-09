#!/usr/bin/node

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const arg1 = parseInt(process.argv[2]);
const fac = factorial(arg1);
console.log(fac);
