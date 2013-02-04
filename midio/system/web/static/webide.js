
function getPatch(doc, patch) {
    $.get('http://raspberrypi.local:8080/patch/' + patch, function(data) {
        doc.setValue(data);
        alert("cool");
    });
}



$(document).ready(function() {


      var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
        mode: {name: "python",
               version: 2,
               singleLineStringErrors: true},
        lineNumbers: true,
        indentUnit: 4,
        tabMode: "shift",
        matchBrackets: true,
      });

  var doc = editor.getDoc();

    getPatch(doc, "treefill");


});
