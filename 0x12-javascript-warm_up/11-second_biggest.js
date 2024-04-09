#!/usr/bin/node
const argCount = process.argv.length - 2;
const args = process.argv.slice(2);

if (argCount === 0 || argCount === 1) {
  console.log(0);
} else {
  args.sort(function (a, b) { return Number(a) - Number(b); });
  console.log(args[args.length - 2]);
}
