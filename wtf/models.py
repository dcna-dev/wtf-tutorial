# coding: utf-8

import datetime
from .db import db

class Noticia(db.Document):
    titulo = db.StringField()
    texto = db.StringField()
    imagem = db.StringField()
    slug_titulo = db.StringField()
    modified = db.DateTimeField(default=datetime.datetime.now)


