import os
import hashlib

from bottle import route, run, template

import config
from styles import NOTELIST_CSS, NOTE_CSS
from javascript import NOTE_JAVASCRIPT

@route('/')
def notelist():
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
    """.format(NOTELIST_CSS, notelist)
    return template(response)

def checkForNoteFolder():
	if not os.path.isdir(config.NOTE_FOLDER_PATH):
		os.makedirs(config.NOTE_FOLDER_PATH)


def hashOfFile(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

@route('/<notename>') 
def viewNote(notename):
    checkForNoteFolder()

    notepath = config.NOTE_FOLDER_PATH + "/" + notename
    try:
        notehash = hashOfFile(notepath)
    except IOError as e:
    	notehash = "new note"

    noteText = ""
    if os.path.isfile(notepath):
    	with open(notepath, 'r') as note:
    		noteText += note.read()

    response = """
        <head>
            <style>
                {}
            </style>
            <script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
            <script src="//cdnjs.cloudflare.com/ajax/libs/showdown/0.3.1/showdown.min.js"></script>
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
                <a href='/'>to note list</a>
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
    """.format(NOTE_CSS, NOTE_JAVASCRIPT, notename, notehash, noteText)
    return template(response)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(server='gunicorn', host='localhost', port=8080)