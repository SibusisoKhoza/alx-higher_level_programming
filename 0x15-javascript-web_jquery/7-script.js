$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (content) => {
  $('DIV#character').text(content.name);
});
