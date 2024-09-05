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

  let j = 0;
  while (data.characters[j] !== undefined) {
    request(data.characters[j], (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const actorInfo = JSON.parse(body);
      console.log(actorInfo.name);
    });

    j = j + 1;
  }
});
