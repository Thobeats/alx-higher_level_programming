#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a < 0) {
    return (1);
  } else {
    if (a > 0) {
      return (a * factorial(a - 1));
    } else {
      return (1);
    }
  }
}
const [, , factorialNum] = process.argv;

console.log(factorial(Number(factorialNum)));
