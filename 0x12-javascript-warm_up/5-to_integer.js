#!/usr/bin/node
//  prints My number: <first argument converted in integer>
//  if the first argument can be converted to an integer

const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(args[2]));
}
