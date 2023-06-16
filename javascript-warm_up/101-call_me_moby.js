#!/usr/bin/node
const callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

callMeMoby(5, function () {
  console.log("C is fun");
});
