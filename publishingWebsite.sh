pelican content -o output -s pelicanconf.py
ghp-import output -b master
git push origin master
