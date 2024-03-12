#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const values = Object.values(dict);
const uniqueVals = [...new Set(values)];
const newDictionary = {};

for (const j in uniqueVals) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === uniqueVals[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDictionary[uniqueVals[j]] = list;
}
console.log(newDictionary);
