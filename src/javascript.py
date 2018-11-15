NOTE_JAVASCRIPT = """
    $(document).ready(function(){
        $("#saveButton").click(function(e){
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
                    location.reload();
                }
            });
        });
        var converter = new Showdown.converter();
        var markdownText = converter.makeHtml($("#noteTextArea").val());
            $("#markdownTextArea").html(markdownText);
        });
"""
