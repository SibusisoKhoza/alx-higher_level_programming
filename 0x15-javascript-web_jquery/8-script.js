$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (content) => {
  const movies = content.results;
  for (const movie in movies) {
    $('#list_movies').append('<li>' + movies[movie].title + '</li>');
  }
});
