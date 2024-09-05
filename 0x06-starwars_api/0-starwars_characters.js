#!/usr/bin/node

const request = require('request');
const args = process.argv;
request('https://swapi-api.alx-tools.com/api/films/' + args[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  // console.log(data);

  let completed = 0
  const allNames = []

   data.characters.forEach((characterUrl, index) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }

      const actorInfo = JSON.parse(body);
      allNames[index] = actorInfo.name;
      completed++;

      if (completed === data.characters.length)
      {
        allNames.forEach(name => console.log(name));
      }
    });

  })
});
