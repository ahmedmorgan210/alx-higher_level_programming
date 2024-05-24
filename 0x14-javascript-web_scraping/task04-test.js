#!/usr/bin/node
const request = require('request-promise-native'); // Using promise version of request

async function getCharactersFromFilm(url) {
    try {
        const response = await request({ uri: url, json: true });
        const characters = response.characters;
        let wedgeCount = 0;

        for (let characterUrl of characters) {
            const characterResponse = await request({ uri: characterUrl, json: true });
            if (characterResponse.name === 'Wedge Antilles') {
                wedgeCount++;
            }
        }

        return wedgeCount;
    } catch (error) {
        console.error("Error fetching data:", error);
        return 0; // Return 0 in case of error to avoid breaking the loop
    }
}

async function countFilmsWithWedge(apiUrl) {
    try {
        const response = await request({ uri: apiUrl, json: true });
        const films = response.results;
        let wedgeCount = 0;

        for (let film of films) {
            const filmWedgeCount = await getCharactersFromFilm(film.url);
            if (filmWedgeCount > 0) {
                wedgeCount++;
            }
        }

        console.log(`Number of films where Wedge Antilles appears: ${wedgeCount}`);
    } catch (error) {
        console.error("Error fetching films:", error);
    }
}

// Assuming the API URL is passed as a command-line argument
if (process.argv.length < 3) {
    console.error("Please provide the API URL as an argument.");
} else {
    const apiUrl = process.argv[2];
    countFilmsWithWedge(apiUrl);
}
