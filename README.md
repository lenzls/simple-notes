# Simple Notes
A tiny application for quick note taking without permissions or other fancy stuff.

Uses the filesystem as a datastore.


![Screenshot](https://raw.githubusercontent.com/lenzls/simple-notes/master/docs/screenshot.png)

## Features

* quick notetaking
* simple concurrent modification protection
* Markdown view
* filesystem as a datastore
* hierarchical notes via subdirectories
* simple note hiding functionality

## Installation

1. `git clone … && cd …`
2. `cp .env.example .env`
3. adapt `.env`-file
4. `pipenv install`

## Usage

1. `pipenv run python3 src/app.py`
2. go to `http://localhost:63636/` to view the list of Notes
3. go to `http://localhost:63636/subdir/noteName` to create/edit the note `noteName` in subdirectory `subdir`

_Note_: notes/directories starting with a dot are hidden in the notelist and can only accessed with the direct link


### Run via supervisord

```
[program:simple-notes]
command=/home/zorilla/.local/bin/pipenv run python3 src/app.py
directory=/home/zorilla/applications/simple-notes
```

restarting: `supervisorctl restart simple-notes`


### Route via .htaccess

```
RewriteEngine On
RewriteBase /
RewriteRule ^(.*)$ http://localhost:63636/$1 [P]
```
