#!/usr/bin/node
const [,, movieId] = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) {
    return console.error(error + response);
  }
  const bodyJson = JSON.parse(body);
  console.log(bodyJson.title);
});
