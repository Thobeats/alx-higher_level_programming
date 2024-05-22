#!/usr/bin/node
const request = require('request');
const [,, url] = process.argv;

const options = {
  url,
  headers: {
    'User-Agent': 'request',
    Accept: 'application/json'
  }
};

request(options, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const completedTasks = JSON.parse(body).filter(todo => todo.completed === true)
    .reduce(function (sum, td) {
      if (!sum[td.userId]) {
        sum[td.userId] = 0;
      }

      sum[td.userId]++;
      return sum;
    }, {});
  console.log(completedTasks);
});
