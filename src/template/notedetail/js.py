NOTEDETAIL_JAVASCRIPT = """
    function addClickHandler(id, fnc) {
        var el = document.getElementById(id);
        if (el.addEventListener) {
            el.addEventListener("click", fnc, false);
        } else {
            el.attachEvent('onclick', fnc);
        }
    }
    $(document).ready(function() {
        addClickHandler("saveButton", writeNote)
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
                location.reload()
            });
            var converter = new showdown.Converter();
            var markdownText = converter.makeHtml($("#noteTextArea").val());
            $("#markdownTextArea").html(markdownText);
        }
    });
"""
