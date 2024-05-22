#!/usr/bin/node
const request = require('request');
const [,, movieId] = process.argv;

const options = {
  url: 'https://swapi-api.alx-tools.com/api/people/',
  headers: {
    'User-Agent': 'request',
    Accept: 'application/json'
  }
};

request(options, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  const films = JSON.parse(body).results.filter(person => person.films.includes(filmUrl));
  for (const flm of films) {
    console.log(flm.name);
  }
});
