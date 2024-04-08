#!/usr/bin/node
const [, , one] = process.argv;
if (isNaN(one)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + one);
}
