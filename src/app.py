import os

from bottle import route, run, template

import config

@route('/list')
def notelist():
    css = """
        body {
        	background-color: rgba(241, 255, 249, 1);
        	font-family: Verdana;
        }
    """
    notelist = "<ul>\n"
    for notefile in sorted([f for f in os.listdir(config.NOTE_FOLDER_PATH) if not f.startswith('.')]):
    	notelist += "<li><a href='{0}'>{0}</a></li>\n".format(notefile)
    notelist += "</ul>\n"

    response = """
    <html>
        <head>
            <style>
                {}
            </style>
        </head>
        <body>
            <h1>Notelist:</h1>
            {}
        </body>
    </html>
    """.format(css, notelist)
    return template(response)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(server='gunicorn', host='localhost', port=8080)