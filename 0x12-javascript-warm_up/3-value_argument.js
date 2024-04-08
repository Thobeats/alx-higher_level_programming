#!/usr/bin/node
const args = process.argv.length - 2;
let response;
if (args === 0) {
  response = 'No argument';
} else if (args > 0) {
  response = '';
  for (let i = 2; i < process.argv.length; i++) {
    response += process.argv[i] + ' ';
  }
}
console.log(response);
