<html>
    <head>
        <meta name="robots" content="noindex" />
        <link rel='stylesheet' type='text/css' href='/static/notes.css'>
    </head>
    <body>
        <h1>Notelist:</h1>
        <ul>
            % for item in notelist:
                <li><a href='{{item}}'>{{item}}</a></li>
            % end
        </ul>
    </body>
</html>
