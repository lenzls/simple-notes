NOTEDETAIL_HTML = """
<html>
    <head>
        <style>
            {}
        </style>
        <script
          src="https://code.jquery.com/jquery-2.2.4.min.js"
          integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
          crossorigin="anonymous"></script>
        <script src="/static/showdown.min.js"></script>
        <script type='text/javascript'>
            {}
        </script>
    </head>
    <body>
        <div>
            <h1>notename:  <span id='noteNameArea'>{}</span></h1>
            <b>notehash:</b> <span id='noteHashArea'>{}</span>
        </div>
        <h4>
            <a href='/list'>to note list</a>
        </h4>
        <div id='textArea'>
            <h2>plain note</h2>
                <textarea id='noteTextArea'>{}</textarea >
            <button id='saveButton'>save</button>
        </div>
        <div id='markdownArea'>
            <h2>markdown of saved note</h2>
            <div id='markdownTextArea'></div>
        </div>
        <div id='debugdiv'></div>
    </body>
</html>
"""
