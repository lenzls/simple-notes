NOTEDETAIL_JAVASCRIPT = """
    function addClickHandler(id, fnc) {
        var el = document.getElementById(id);
        if (el.addEventListener) {
            el.addEventListener("click", fnc, false);
        } else {
            el.attachEvent('onclick', fnc);
        }
    }

    document.addEventListener("DOMContentLoaded", function() {
        addClickHandler("saveButton", writeNote)
        function writeNote() {
            fetch('/writeNote', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                },
                body:
                    JSON.stringify({
                        "noteName" : document.getElementById("noteNameArea").textContent,
                        "noteText" : document.getElementById("noteTextArea").value,
                        "noteHash" : document.getElementById("noteHashArea").textContent
                    })
            })
            .then(response => response.blob())
            .then(resp => {
                console.log(resp)
                window.location = "/" + resp.createdNote;
                location.reload()
            });
        }

        var converter = new showdown.Converter();
        var markdownText = converter.makeHtml(document.getElementById("noteTextArea").value);
        document.getElementById("markdownTextArea").innerHTML = markdownText;
    });
"""
