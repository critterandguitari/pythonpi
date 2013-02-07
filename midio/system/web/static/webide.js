editor = null
currentPatch = ''


function getPatch(patch) {
    $.get('http://raspberrypi.local:8080/get_patch/' + patch, function(data) {
        editor.setValue(data);
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
           $("#patches").append($patch);
        });
    });
}

function savePatch() {
    
    $.post("http://raspberrypi.local:8080/save", { name: currentPatch, contents: editor.getValue() })
    .done(function(data) {
         // alert(data);
    });
}

$(document).ready(function() {
    
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/merbivore_soft");
    editor.getSession().setMode("ace/mode/python");
    //$("#editor").style.fontSize='16px';
    document.getElementById('editor').style.fontSize='16px';
    getPatchList();

    $("#save").click(function() {
        savePatch(editor);
    });

});
