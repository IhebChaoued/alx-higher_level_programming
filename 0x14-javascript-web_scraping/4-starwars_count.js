#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) =>
      movie.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count
    , 0));
  }
});
