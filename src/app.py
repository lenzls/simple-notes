import os
import hashlib

from bottle import route, post, run, template, request

from template.notelist.html import NOTELIST_HTML
from template.notelist.css import NOTELIST_CSS
from template.notedetail.html import NOTEDETAIL_HTML
from template.notedetail.css import NOTEDETAIL_CSS
from template.notedetail.js import NOTEDETAIL_JAVASCRIPT

NOTE_FOLDER_PATH = os.getenv('NOTE_FOLDER_PATH', './default_notes_location')

def createDirsIfNecessary(dirpath):
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)

def hashOfFile(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

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

@route('/')
@route('/list')
def notelist():
    createDirsIfNecessary(NOTE_FOLDER_PATH)

    notelist = "<ul>\n"
    for notefile in sorted(getListOfNotePaths()):
        notelist += "<li><a href='{0}'>{0}</a></li>\n".format(notefile)
    notelist += "</ul>\n"

    response = NOTELIST_HTML.format(NOTELIST_CSS, notelist)
    return template(response)


def getListOfNotePaths():
    listOfFiles = []
    for (dirpath, dirnames, filenames) in os.walk(NOTE_FOLDER_PATH):
        dirPathWithoutNotesFolder = dirpath[len(NOTE_FOLDER_PATH) + 1:]
        if dirPathWithoutNotesFolder.startswith('.'):
            continue
        for filename in filenames:
            if filename.startswith('.'):
                continue
            path = os.path.join(dirPathWithoutNotesFolder, filename)
            listOfFiles.append(path)
    return listOfFiles

@route('/<notename:path>')
def viewNote(notename):
    createDirsIfNecessary(NOTE_FOLDER_PATH)

    notepath = NOTE_FOLDER_PATH + "/" + notename
    try:
        notehash = hashOfFile(notepath)
    except IOError as e:
        notehash = "new note"

    noteText = ""
    if os.path.isfile(notepath):
        with open(notepath, 'r') as note:
            noteText += note.read()

    response = NOTEDETAIL_HTML.format(NOTEDETAIL_CSS, NOTEDETAIL_JAVASCRIPT, notename, notehash, noteText)
    return template(response)

run(server='gunicorn', host='localhost', port=63636)
