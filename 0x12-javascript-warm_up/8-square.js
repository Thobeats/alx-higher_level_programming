#!/usr/bin/node
const [, , occurence] = process.argv;
if (isNaN(occurence)) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  let mySquare = '';

  while (j < occurence) {
    mySquare += 'X';
    j++;
  }

  while (i < occurence) {
    console.log(mySquare);
    i++;
  }
}
