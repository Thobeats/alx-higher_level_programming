#!/usr/bin/node
const request = require('request');
const [,, movieId] = process.argv;
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';
const allCharacters = [];

const options = {
  url: filmUrl,
  headers: {
    'User-Agent': 'request',
    Accept: 'application/json'
  }
};

function starWarsCharacters (characterUrl, index, size) {
  request(characterUrl, (error, response, res) => {
    if (error) {
      return console.error(error);
    }
    const characterBody = JSON.parse(res);
    allCharacters[index] = characterBody.name;
    if (allCharacters.length === size && !allCharacters.includes(undefined)) {
      allCharacters.forEach(chr => console.log(chr));
    }
  });
}

request(options, (error, response, body) => {
  if (error) {
    return console.error(error);
  }

  const bodyJson = JSON.parse(body).results[movieId - 1];

  for (const character in bodyJson.characters) {
    starWarsCharacters(bodyJson.characters[character], character, bodyJson.characters.length);
  }
});
