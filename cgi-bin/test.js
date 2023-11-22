#!/usr/bin/node
const fs = require('fs');

console.log('Content-Type: text/plain\n\nHello World!');

console.log('\nEnvironment:');
console.log(process.env);

console.log('\nInput:');
console.log(fs.readFileSync(process.stdin.fd, 'utf-8'));
