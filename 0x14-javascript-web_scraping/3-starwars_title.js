#!/usr/bin/node
const [,, movieId] = process.argv;
const { response } = require('express');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  bodyJson = JSON.parse(body)
  console.log(bodyJson.title) 
});
