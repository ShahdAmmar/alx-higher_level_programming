#!/usr/bin/node

const dct = require('./101-data').dict;

const items = Object.entries(dct);
const values = Object.values(dct);
const uniqValues = [...new Set(values)];

const newDct = {};
for (const i in uniqValues) {
  const lst = [];
  for (const j in items) {
    if (items[j][1] === uniqValues[i]) {
      lst.push(items[j][0]);
    }
  }
  newDct[uniqValues[i]] = lst;
}
console.log(newDct);
