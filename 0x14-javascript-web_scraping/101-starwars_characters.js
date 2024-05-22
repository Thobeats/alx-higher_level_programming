#!/usr/bin/node
const request = require('request');
const [,, movieId] = process.argv;
const filmUrl = `https://swapi-api.alx-tools.com/api/films/`;

const options = {
  url: filmUrl,
  headers: {
    'User-Agent': 'request',
    Accept: 'application/json'
  }
};

request(options, (error, response, body) => {
  if (error) {
    return console.error(error);
  }

  const bodyJson = JSON.parse(body);
  for (const character of bodyJson.results[movieId - 1].characters) {
    request(character, (error, response, res) => {
      if (error) {
        return console.error(error);
      }

      const characterBody = JSON.parse(res);
      console.log(characterBody.name);
    });
  }
});
