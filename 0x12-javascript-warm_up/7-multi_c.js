#!/usr/bin/node
const [, , occurence] = process.argv;
if (isNaN(occurence)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < occurence) {
    console.log('c is fun');
    i++;
  }
}
