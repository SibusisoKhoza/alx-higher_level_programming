#!/usr/bin/node
/*
Write a script that concats 2 files.

The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/
const fs = require('fs');

// Check if correct number of arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

// Read content of fileA
fs.readFile(fileA, 'utf8', (errA, dataA) => {
  if (errA) {
    console.error(`Error reading ${fileA}: ${errA}`);
    process.exit(1);
  }

  // Read content of fileB
  fs.readFile(fileB, 'utf8', (errB, dataB) => {
    if (errB) {
      console.error(`Error reading ${fileB}: ${errB}`);
      process.exit(1);
    }

    // Concatenate contents of fileA and fileB
    const concatenatedContent = `${dataA}${dataB}`;

    // Write concatenated content to fileC
    fs.writeFile(fileC, concatenatedContent, (errWrite) => {
      if (errWrite) {
        console.error(`Error writing to ${fileC}: ${errWrite}`);
        process.exit(1);
      }
      console.log(`Concatenated files ${fileA} and ${fileB} into ${fileC}`);
    });
  });
});
