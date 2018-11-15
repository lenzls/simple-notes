NOTEDETAIL_JAVASCRIPT = """
    $(document).ready(function(){
        var el = document.getElementById("saveButton");
        if (el.addEventListener) {
            el.addEventListener("click", writeNote, false);
        } else {
            el.attachEvent('onclick', writeNote);
        }
        function writeNote() {
            fetch('/writeNote', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                },
                body:
                    JSON.stringify({
                        "noteName" : $("#noteNameArea").text(),
                        "noteText" : $("#noteTextArea").val(),
                        "noteHash" : $("#noteHashArea").text()
                    })
            })
            .then(response => response.blob())
            .then(resp => {
                console.log(resp)
                window.location = "/" + resp.createdNote;
            });
            var converter = new showdown.Converter();
            var markdownText = converter.makeHtml($("#noteTextArea").val());
            $("#markdownTextArea").html(markdownText);
        }
    });
"""
