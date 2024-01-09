#!/usr/bin/node

const argvlst = process.argv.slice(2);
const nums = argvlst.map(arg => parseInt(arg));

if (argvlst.length <= 1) {
  console.log(0);
} else {
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
