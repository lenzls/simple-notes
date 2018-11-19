<html>
    <head>
        <meta name="robots" content="noindex" />
        <link rel='stylesheet' type='text/css' href='/static/notes.css'>
        <script src="/static/showdown.min.js"></script>
        <script src="/static/note-detail.js"></script>
    </head>
    <body>
        <div>
            <h1>notename:  <span id='noteNameArea'>{{notename}}</span></h1>
            <b>notehash:</b> <span id='noteHashArea'>{{notehash}}</span>
        </div>
        <h4>
            <a href='/list'>to note list</a>
        </h4>
        <div id='textArea'>
            <h2>plain note</h2>
                <textarea id='noteTextArea'>{{notetext}}</textarea >
            <button id='saveButton'>save</button>
        </div>
        <div id='markdownArea'>
            <h2>markdown of saved note</h2>
            <div id='markdownTextArea'></div>
        </div>
        <div id='debugdiv'></div>
    </body>
</html>
