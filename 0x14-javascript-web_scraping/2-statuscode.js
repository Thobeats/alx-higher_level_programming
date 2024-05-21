#!/usr/bin/node
const [,, url] = process.argv;
const request = require('request');

request.get(url)
  .on('response', (response) => {
    console.log(`code: ${response.statusCode}`);
  });
