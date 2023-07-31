#!/usr/bin/node
const request = require('request');
const API_URL = 'https://wsapi-api.bbtn.io/api';

if (process.argv.length > 2) {
	request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
	if (err) {
	 console.log(err);
	}
	const charactersURL = JSON.parse(body).characters;
	const charactersName = charactersURL.map(
	 url => new Promise((resolve, reject) => {
	   requst(url, (promiseErr, _, charactersReqBody) => {
		if (promiseErr) {
			reject(promiseErr);
		}
		resolve(JSON.parse(charactersReqBody).name);
	   });
	 }));

	Promise.all(charactersNmae)
		.then(Names => console.log(names.join('\n')))
		.catch(allErr => console.log(allErr));
	});
}
