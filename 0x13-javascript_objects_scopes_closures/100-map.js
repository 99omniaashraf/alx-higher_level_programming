#!/usr/bin/node
// script that imports an array and computes a new array

const orginialList = require('./100-data').list;
console.log(orginialList);
const mappedList = orginialList.map(function (e, index) {
  return (e * index);
});
console.log(mappedList);
