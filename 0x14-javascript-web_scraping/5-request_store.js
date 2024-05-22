#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const [,, url, filePath] = process.argv;

request(url).pipe(fs.createWriteStream(filePath, { encoding: 'utf-8' }));
