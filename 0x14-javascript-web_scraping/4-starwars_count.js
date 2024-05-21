#!/usr/bin/node
const [,, url] = process.argv;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    return console.error(error + response);
  }
 
  const bodyJson = JSON.parse(body);
  let movies = bodyJson.results.filter((record) => {
    return record.characters.indexOf("https://swapi-api.alx-tools.com/api/people/18/") != -1
  })
  console.log(movies.length);
});
