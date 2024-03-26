#!/usr/bin/node
// Prints the title of a Star Wars movie where
// the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true }, (err, res, body) => {
  if (err) console.log(err);
  console.log(body.title);
});
