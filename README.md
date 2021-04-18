Hindi Lang Image OCR
--------------------

Django Application using `TesserOCR` and `pytesseract` library

Currently deployed a demo at https://ravip18596.pythonanywhere.com/

## Steps to run locally

1) Set necessary env vars for MySQL database connection [foreignLangOCR/wsgi.py](foreignLangOCR/wsgi.py)
2) Run at the root of repo `gunicorn --bind 127.0.0.1:8000 foreignLangOCR.wsgi:application`

## Run docker container

`docker-compose -f docker-compose.yml up`
