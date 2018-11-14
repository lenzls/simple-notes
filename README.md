# .env
```
NOTE_FOLDER_PATH=./notes                                      
```

# .htaccess
```
RewriteEngine On
RewriteBase /
RewriteRule ^(.*)$ http://localhost:63636/$1 [P]
```

# supervisord
restarting: `supervisorctl restart simple-notes`

## script
```
[program:simple-notes]
command=/home/zorilla/.local/bin/pipenv run python3 src/app.py
directory=/home/zorilla/applications/simple-notes
```
