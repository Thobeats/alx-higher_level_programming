// Write a JavaScript script that fetches the character name
// from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (res) {
  $('DIV#character').text(res.name);
});
