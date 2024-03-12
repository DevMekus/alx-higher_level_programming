#!/usr/bin/node
const fs = require('fs');

const fArgument = fs.readFileSync(process.argv[2]).toString();
const sArgument = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArgument + sArgument);
