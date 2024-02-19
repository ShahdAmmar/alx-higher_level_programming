#!/usr/bin/node

const lst = require('./100-data').list;
const newlst = lst.map((x, idx) => x * idx);
console.log(lst);
console.log(newlst);
