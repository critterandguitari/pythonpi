doc = null
currentPatch = ''


function getPatch(patch) {
    $.get('http://raspberrypi.local:8080/get_patch/' + patch, function(data) {
        doc.setValue(data);
        currentPatch = patch
    });
}

function getPatchList() {
     $.getJSON('http://raspberrypi.local:8080', function(data) {
        $.each(data, function (i,v) {
          
            $patch = $('<div></div>').append(v);
            $patch.click(function () {
                getPatch(v);
            });
           $("#owen").append($patch);
        });
    });
}

function savePatch() {
    
    $.post("http://raspberrypi.local:8080/save", { name: currentPatch, contents: doc.getValue() })
    .done(function(data) {
          alert(data);
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

    editor.setSize(1000, '100%');
    doc = editor.getDoc();

    getPatch(doc, "treefill");

    getPatchList();

    $("#save").click(function() {
        savePatch();
    });

});
