NOTEDETAIL_JAVASCRIPT = """
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
                    window.location = "/" + msg.createdNote;
                }
            });
        });
        var converter = new Showdown.converter();
        var markdownText = converter.makeHtml($("#noteTextArea").val());
            $("#markdownTextArea").html(markdownText);
        });
"""
