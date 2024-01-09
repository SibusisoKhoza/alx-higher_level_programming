#!/usr/bin/node
/*
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

*/
const { dict } = require('./101-data');

// Create a new object to store occurrences as keys and user IDs as values
const occurrencesDict = {};

// Loop through the original dictionary to populate the occurrencesDict
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }
  occurrencesDict[occurrences].push(userId);
}

// Printing the new dictionary at the end
console.log(occurrencesDict);
