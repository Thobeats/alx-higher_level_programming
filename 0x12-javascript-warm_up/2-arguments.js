#!/usr/bin/node
const args = process.argv.length - 2;
let response;
if (args === 0) {
  response = 'No argument';
} else if (args === 1) {
  response = 'Argument found';
} else {
  response = 'Arguments found';
}
console.log(response);
