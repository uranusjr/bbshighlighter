(function ($, CodeMirror) {

function selectAll() {
  var div = $('#rendered').get(0);
  var range;
  if (document.body.createTextRange) {
    range = document.body.createTextRange();
    range.moveToElementText(div);
    range.select();
  }
  else if (window.getSelection) {
     var selection = window.getSelection();
     range = document.createRange();
     range.selectNodeContents(div);
     selection.removeAllRanges();
     selection.addRange(range);
  }
}

var editor = CodeMirror.fromTextArea(document.getElementById('id_code'), {
  'autofocus': true,
  'lineNumbers': true
});

$('#function_highlight').click(function () {
  var value = editor.getValue();
  var lexer_name = $('#id_language').val();
  var url = RENDER_URL;
  if (lexer_name)
    url = RENDER_URL + lexer_name + '/';
  $.post(url, {'code': value}).done(function (data) {
    data = data
      .replace(/&/g,'&amp;')
      .replace(/</g,'&lt;').replace(/>/g,'&gt;')
      .replace(/\r?\n/g, '<br>')
      .replace(/ /g, '&nbsp;');
    $('#rendered').html(data);
    selectAll();
  }).fail(function (data) {
    console.log(data);
  });
});

$('#function_select_all').click(function () {
  selectAll();
});

$('#tabs').tabs({'active': 1});

})(jQuery, CodeMirror);
