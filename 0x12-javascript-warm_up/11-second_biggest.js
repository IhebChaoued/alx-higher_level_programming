#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedUniqueNumbers = [...new Set(numbers)].sort((a, b) => b - a);
  console.log(sortedUniqueNumbers[1]);
}
