#!/usr/bin/node
// Prints the number of movies where
// the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const count = body.split('/people/18/').length - 1;
  console.log(count);
});
