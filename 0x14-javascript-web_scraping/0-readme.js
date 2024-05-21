#!/usr/bin/node
const [,, newFile] = process.argv;
const fs = require('fs');

fs.readFile(newFile, 'utf-8', (err, data) => {
  if (err) {
    return console.error(err);
  }

  console.log(data.toString());
});
