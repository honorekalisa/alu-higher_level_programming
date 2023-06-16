#!/usr/bin/node
const executeNTimes = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

function callMeMoby() {
  console.log("C is fun");
}

executeNTimes(5, callMeMoby);
