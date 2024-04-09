#!/usr/bin/node

let noPrinted = 0;
exports.logMe = function (item) {
  console.log(noPrinted + ': ' + item);
  ++noPrinted;
};
