// Write a JavaScript script that fetches and lists the title
// for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (res) {
  $.each(res.results, (key, value) => {
    $('UL#list_movies').append(`<li>${value.title}</li>`);
  });
});
