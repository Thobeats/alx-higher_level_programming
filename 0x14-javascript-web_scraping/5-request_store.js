#!/usr/bin/node
// script that counts the number of films Wedge Antilles is in
const request = require('request');
const fs = require('fs')
const [,, url, filePath] = process.argv;

request(url).pipe(fs.createWriteStream(filePath, { encoding: 'utf-8'}))
