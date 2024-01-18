#!/path/to/your/node
const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api';

if (process.argv.length <= 2) {
  console.error('Please provide the Movie ID as a command-line argument.');
  process.exit(1);
}

const movieId = process.argv[2];

request(`${apiUrl}/films/${movieId}/`, (err, _, body) => {
  if (err) {
    console.error('Error fetching film data:', err);
    process.exit(1);
  }

  const charactersURL = JSON.parse(body).characters;

  const getCharacterName = url => new Promise((resolve, reject) => {
    request(url, (requestErr, __, charactersReqBody) => {
      if (requestErr) {
        reject(requestErr);
      } else {
        resolve(JSON.parse(charactersReqBody).name);
      }
    });
  });

  const charactersNamePromises = charactersURL.map(getCharacterName);

  Promise.all(charactersNamePromises)
    .then(names => {
      console.log(names.join('\n'));
    })
    .catch(allErr => {
      console.error('Error fetching character names:', allErr);
      process.exit(1);
    });
});
