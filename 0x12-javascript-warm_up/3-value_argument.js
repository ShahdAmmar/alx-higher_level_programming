#!/usr/bin/node

const argvlst = process.argv
if (argvlst[2]) {
	console.log(argvlst[2]);
}
else {
	console.log('No argument');
}
