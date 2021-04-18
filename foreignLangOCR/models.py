from django.db import models
from datetime import datetime


class Document(models.Model):
    image = models.ImageField(upload_to =f'uploads/{datetime.now().strftime("%Y/%m/%d")}')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    ocr = models.TextField(blank=True,null=True)
