#!/usr/bin/node
// script that imports a dictionary of occurrences by user
// id and computes a dictionary of user ids by occurrence

const dict = require('./101-data').dict;
console.log(Object.entries(dict).reduce(function (accumulator, current) {
  accumulator[current[1]] = (accumulator[current[1]] || []).concat(current[0]);
  return accumulator;
}, {}));
