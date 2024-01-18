#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide the Movie ID as a command-line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status Code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);

  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, characterBody) {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status Code:', response.statusCode);
        process.exit(1);
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
