#!/usr/bin/node
const fs = require('fs').promises;

async function readFile(filePath) {
    try {
        const data = await fs.readFile(filePath);
        console.log(data.toString());
    } catch (error) {
        console.error(error);
    }
}
readFile(process.argv[2])
