#!/usr/bin/node
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
const [, , first, second] = process.argv;
if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  add(first, second);
}
