// Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    $lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${$lang}`;
    $.get(url, function (res) {
      $('DIV#hello').text(`${res.hello}`);
    });
  });
});
