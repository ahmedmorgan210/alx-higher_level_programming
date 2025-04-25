#!/usr/bin/node

const fs = require('fs');

// Get file paths from command-line arguments
const [,, file1, file2, dest] = process.argv;

// Read the contents of both files
const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');

// Combine contents with a newline in between
const combinedContent = content1 + '\n' + content2;

// Write the combined content to the destination file
fs.writeFileSync(dest, combinedContent);
