#!/usr/bin/node

const fs = require('fs');

// Get file paths from command-line arguments
const [,, file1, file2, dest] = process.argv;

// Read the contents of both files
const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');

// Initialize combined content
let combinedContent = '';

// Handle cases where one or both files are empty
if (content1 && content2) {
  combinedContent = content1 + '\n' + content2;
} else if (content1) {
  combinedContent = content1;
} else if (content2) {
  combinedContent = content2;
} // else both are empty, combinedContent remains empty

// Write the combined content to the destination file
fs.writeFileSync(dest, combinedContent);
