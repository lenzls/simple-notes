import os
import hashlib

from bottle import route, post, run, template, request

from styles import NOTELIST_CSS, NOTE_CSS
from javascript import NOTE_JAVASCRIPT

NOTE_FOLDER_PATH = os.getenv('NOTE_FOLDER_PATH', './default_notes_location')

@post('/writeNote')
def writeNote():
    notename = request.forms["noteName"]
    notetext = request.forms["noteText"]
    notepath = NOTE_FOLDER_PATH + "/" + notename
    notedir = "/".join(notepath.split("/")[0:-1])
    createDirsIfNecessary(notedir)
    oldNotehash = request.forms["noteHash"]
    try:
        newNotehash = hashOfFile(notepath)

        if oldNotehash == newNotehash:
            #nobody modified the note during your session
            with open(notepath, 'w') as note:
                note.write(str(notetext))
        else:
            #somebody modigied the note during your session
            #print "!!! file was modified saved under <note>.alt !!!"
            with open(notepath + ".alt", 'w') as note:
                note.write(str(notetext))
    except IOError as e:
        with open(notepath, 'w') as note:
            note.write(str(notetext))

def getListOfNotePaths():
    listOfFiles = []
    for (dirpath, dirnames, filenames) in os.walk(NOTE_FOLDER_PATH):
        listOfFiles += [os.path.join(dirpath, file)[len(NOTE_FOLDER_PATH) + 1:] for file in filenames]
    return listOfFiles

@route('/')
@route('/list')
def notelist():
    checkForNoteFolder()

    notelist = "<ul>\n"
    for notefile in sorted([f for f in getListOfNotePaths() if not f.startswith('.')]):
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
    createDirsIfNecessary(NOTE_FOLDER_PATH)

def createDirsIfNecessary(dirpath):
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)

def hashOfFile(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

@route('/<notename:path>')
def viewNote(notename):
    checkForNoteFolder()

    notepath = NOTE_FOLDER_PATH + "/" + notename
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
            <script
			  src="https://code.jquery.com/jquery-2.2.4.min.js"
			  integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
			  crossorigin="anonymous"></script>
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
    """.format(NOTE_CSS, NOTE_JAVASCRIPT, notename, notehash, noteText)
    return template(response)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(server='gunicorn', host='localhost', port=63636)
