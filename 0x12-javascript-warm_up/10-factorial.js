#!/usr/bin/node
function factorial (a) {
  if (a >= 0) {
    return (parseInt(a) + parseInt(factorial(a - 1)));
  }
  return 0;
}
const [, , factorialNum] = process.argv;
if (isNaN(factorialNum) || factorialNum < 0) {
  console.log(1);
} else {
  console.log(factorial(factorialNum));
}
