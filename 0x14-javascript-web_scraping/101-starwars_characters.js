#!/usr/bin/node
const request = require('request');
const [,, movieId] = process.argv;
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const options = {
  url: filmUrl,
  headers: {
    'User-Agent': 'request',
    Accept: 'application/json'
  }
};

function starWarsCharacters (characters, start, end) {
  if (start === end) {
    return;
  }

  request(characters[start], (error, response, res) => {
    if (error) {
      return console.error(error);
    }
    const characterBody = JSON.parse(res);
    console.log(characterBody.name);
  });

  start++;
  starWarsCharacters(characters, start, end);
}

request(options, (error, response, body) => {
  if (error) {
    return console.error(error);
  }

  const bodyJson = JSON.parse(body);
  starWarsCharacters(bodyJson.characters, 0, bodyJson.characters.length);
});
