NOTEDETAIL_JAVASCRIPT = """
    $(document).ready(function(){
        var el = document.getElementById("saveButton");
        if (el.addEventListener) {
            el.addEventListener("click", writeNote, false);
        } else {
            el.attachEvent('onclick', writeNote);
        }

        function writeNote(e){
            e.preventDefault();
            jQuery.ajax({
                type: "POST",
                url: "/writeNote",
                data: {
                    "noteName" : $("#noteNameArea").text(),
                    "noteText" : $("#noteTextArea").val(),
                    "noteHash" : $("#noteHashArea").text()
                },
                success: function (msg) {
                    window.location = "/" + msg.createdNote;
                }
            });
        };
        var converter = new showdown.Converter();
        var markdownText = converter.makeHtml($("#noteTextArea").val());
            $("#markdownTextArea").html(markdownText);
        });
"""
