#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let noOfOccurence = 0;
  list.forEach((l) => {
    if (l === searchElement) {
      ++noOfOccurence;
    }
  });

  return noOfOccurence;
};
