FROM python:3.8-buster

RUN chmod 666 /var/log

WORKDIR /app

RUN pip install --upgrade pip

ADD ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get -y install tesseract-ocr libtesseract-dev libleptonica-dev

RUN CPPFLAGS=-I/tessdata pip install tesserocr

RUN pip install -r requirements.txt

COPY . .

RUN pip install gunicorn

ENV PYTHONUNBUFFERED 1

EXPOSE 6050

CMD ["gunicorn",  "--bind", "0.0.0.0:6050", "foreignLangOCR.wsgi:application"]