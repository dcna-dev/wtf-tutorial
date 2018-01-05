# coding: utf-8

import os
from werkzeug import secure_filename
from flask import (
        Blueprint, request, current_app,
        send_from_directory, render_template
    )
from slugify import slugify

from ..models import Noticia
from flask_security import login_required # decorator
from ..cache import cache

noticias_blueprint = Blueprint('noticias', __name__)

@noticias_blueprint.route("/noticias/cadastro", methods=["GET", "POST"])
@login_required # The login will be verified here
def cadastro():
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename
        nova_noticia = Noticia.objects.create(**dados_do_formulario)
        nova_noticia.slug_titulo = slugify(nova_noticia.titulo, to_lower=True)
        nova_noticia.save()
        return render_template('cadastro_sucesso.html', titulo=nova_noticia.titulo, slug_titulo=nova_noticia.slug_titulo)

    return render_template('cadastro.html', title=u"Inserir nova noticia")


@noticias_blueprint.route("/")
@cache.cached(timeout=300)
def index():
    todas_as_noticias = Noticia.objects.all()
    return render_template('index.html',
                            noticias=todas_as_noticias,
                            title=u"Todas as notícias")

@noticias_blueprint.route("/noticia/<slug_titulo>")
def noticia(slug_titulo):
    noticia_cacheada = cache.get(slug_titulo)
    if noticia_cacheada:
        noticia = noticia_cacheada
    else:
        noticia = Noticia.objects.get(slug_titulo=slug_titulo)
        cache.set(slug_titulo, noticia, timeout=300)
    return render_template('noticia.html', noticia=noticia)

@noticias_blueprint.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)


