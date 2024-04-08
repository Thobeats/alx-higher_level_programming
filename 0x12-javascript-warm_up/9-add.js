#!/usr/bin/node
const [, , first, second] = process.argv;
if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  console.log(first + second);
}
