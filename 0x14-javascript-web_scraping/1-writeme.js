#!/usr/bin/node
const [,, filePath, data] = process.argv;
const fs = require('fs');

const options = {
  encoding: 'utf-8',
  flag: 'w'
};

fs.writeFile(filePath, data, options, (err) => {
  if (err) {
    return console.error(err);
  }
});
