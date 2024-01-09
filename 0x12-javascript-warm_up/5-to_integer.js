#!/usr/bin/node

const arg1int = parseInt(process.argv[2]);
if (arg1int) {
  console.log('My number: ' + arg1int);
} else {
  console.log('Not a number');
}
