#!/usr/bin/node

const num1 = process.argv[2];
const num2 = process.argv[3];
const result = add(num1, num2);

function add(a, b) {
	return parseInt(num1) + parseInt(num2);
}
console.log(result || 'NaN');
