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

request(options, (error, response, body) => {
  if (error) {
    return console.error(error);
  }

  let bodyJson = JSON.parse(body)
  for (let character of bodyJson.characters) {
    request(character, (error, response, res) => {
      if (error) {
        return console.error(error);
      }

      let characterBody = JSON.parse(res)
      console.log(characterBody.name)
    });
    
  }
});
