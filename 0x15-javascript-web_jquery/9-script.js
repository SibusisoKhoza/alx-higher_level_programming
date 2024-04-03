$.get('https://fourtonfish.com/hellosalut/?lang=fr', (content) => {
  $('DIV#hello').text(content.hello);
});
