#!/usr/bin/node
function add(a, b) {
  return (parseInt(a) + parseInt(b));
}
const [, , first, second] = process.argv;
if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  console.log(add(first, second));
}
