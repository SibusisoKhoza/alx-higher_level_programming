#!/usr/bin/node

const { list } = require('./100-data');

// Using map to create a new array where each value is multiplied by its index
const newList = list.map((value, index) => value * index);

// Printing the initial list and the new list
console.log(list);
console.log(newList);
