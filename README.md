#supervisord script
[program:simple-notes]
command=/home/zorilla/.local/bin/pipenv run python3 src/app.py
directory=/home/zorilla/applications/simple-notes

#.htaccess
RewriteEngine On
RewriteBase /
RewriteRule ^(.*)$ http://localhost:63636/$1 [P]