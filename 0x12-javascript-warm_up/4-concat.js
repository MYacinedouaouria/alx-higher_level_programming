#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const args = process.argv;
const arg1 = args[2];
const arg2 = args[3];
const sentence = arg1 + ' is ' + arg2;
console.log(sentence);
