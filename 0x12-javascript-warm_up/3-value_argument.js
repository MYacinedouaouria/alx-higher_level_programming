#!/usr/bin/node
// prints the first argument passed

const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
