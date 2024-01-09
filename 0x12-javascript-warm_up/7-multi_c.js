#!/usr/bin/node

const arg1int = parseInt(process.argv[2]);
if (arg1int) {
  for (let i = 0; i < arg1int; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
