#!/usr/bin/node
const args = process.argv.length - 2;
if (args === 0) {
  console.log('No argument');
} else if (args > 0) {
  const response = process.argv.slice(2);
  console.log(response[0]);
}
