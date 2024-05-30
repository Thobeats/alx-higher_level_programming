// Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
// Include the Enter Key

$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});

function translate () {
  $lang = $('INPUT#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${$lang}`;
  $.get(url, function (res) {
    $('DIV#hello').text(`${res.hello}`);
  });
}
