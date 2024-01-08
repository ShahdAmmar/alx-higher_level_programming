#!/usr/bin/node

const argvlen = process.argv.length;

if (argvlen === 2) {
	console.log('No argument');
} else if (argvlen === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
