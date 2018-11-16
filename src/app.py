import os

from bottle import route, post, run, request, static_file, template, TEMPLATE_PATH

from utils import createDirsIfNecessary, hashOfFile

NOTE_FOLDER_PATH = os.getenv("NOTE_FOLDER_PATH", "./default_notes_location")
NOTE_OVERWRITE_PROTECTION_SUFFIX = ".alt"
TEMPLATE_DIRECTORY = "./src/templates/"

currentModulePath = os.path.dirname(os.path.realpath(__file__))

@route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root=os.path.join(currentModulePath, "static"))

@post("/writeNote")
def writeNote():
    notename = request.json["noteName"]
    notetext = request.json["noteText"]
    rememberedNotehash = request.json["noteHash"]
    notepath = NOTE_FOLDER_PATH + "/" + notename
    notedir = "/".join(notepath.split("/")[0:-1])
    createDirsIfNecessary(notedir)

    if os.path.exists(notepath):
        currentNoteHash = hashOfFile(notepath)
        if rememberedNotehash != currentNoteHash:
            notename += NOTE_OVERWRITE_PROTECTION_SUFFIX
            notepath += NOTE_OVERWRITE_PROTECTION_SUFFIX
    try:
        with open(notepath, "w") as note:
            note.write(str(notetext))
    except IOError as e:
        return HTTPResponse(status=500, body="IO Error during note creation")
    return {
        "createdNote": notename
    }

@route("/")
@route("/list")
def notelist():
    createDirsIfNecessary(NOTE_FOLDER_PATH)
    return template("note-list", notelist=sorted(getListOfNotePaths()))

def getListOfNotePaths():
    listOfFiles = []
    for (dirpath, dirnames, filenames) in os.walk(NOTE_FOLDER_PATH):
        dirPathWithoutNotesFolder = dirpath[len(NOTE_FOLDER_PATH) + 1:]
        if dirPathWithoutNotesFolder.startswith("."):
            continue
        for filename in filenames:
            if filename.startswith("."):
                continue
            path = os.path.join(dirPathWithoutNotesFolder, filename)
            listOfFiles.append(path)
    return listOfFiles

@route("/<notename:path>")
def viewNote(notename):
    createDirsIfNecessary(NOTE_FOLDER_PATH)

    notepath = NOTE_FOLDER_PATH + "/" + notename
    try:
        notehash = hashOfFile(notepath)
    except IOError as e:
        notehash = "new note"

    noteText = ""
    if os.path.isfile(notepath):
        with open(notepath, "r") as note:
            noteText += note.read()

    return template("note-detail", notename=notename, notehash=notehash, notetext=noteText)

TEMPLATE_PATH.insert(0, TEMPLATE_DIRECTORY)
run(server="gunicorn", host="localhost", port=63636)
