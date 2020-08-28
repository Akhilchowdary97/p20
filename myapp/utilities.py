import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","p20.settings")

import django
django.setup()

from django.core.files.storage import FileSystemStorage

def store_Image(Image):
    fs=FileSystemStorage()
    file=fs.save(Image.name,Image)
    file_url=fs.url(file)
    return file_url