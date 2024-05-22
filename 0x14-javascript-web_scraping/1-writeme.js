#!/usr/bin/node
const fs = require('fs').promises;

async function writFile (filePath, text) {
  try {
    await fs.writeFile(filePath, text);
  } catch (error) {
    console.error(error);
  }
}

writFile(process.argv[2], process.argv[3]);
