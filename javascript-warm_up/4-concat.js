#!/usr/bin/node
const argument1 = process.argv[2];
const argument2 = process.argv[3];

if (argument1 === undefined || argument2 === undefined) {
  console.log('Two arguments are required');
} else {
  console.log(`${argument1} is ${argument2}`);
}