"""
Este archivo contiene una aplicación web basica en flask.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Devuelve la página principal de Inicio de la web"""
    return render_template('index.html', current_page='index')


@app.route('/actividades')
def actividades():
    """Devuelve la página de actividades de la web"""
    return render_template('actividades.html', current_page='actividades')


@app.route('/gastronomia')
def gastronomia():
    """Devuelve la página de gastronomía de la web"""
    return render_template('gastronomia.html', current_page='gastronomia')


@app.route('/cultura')
def cultura():
    """Devuelve la página de cultura de la web"""
    return render_template('cultura.html', current_page='cultura')


@app.route('/idioma')
def idioma():
    """Devuelve la página de idioma de la web"""
    return render_template('idioma.html', current_page='idioma')


@app.route('/contacto')
def contacto():
    """Devuelve la página de contacto de la web"""
    return render_template('contacto.html', current_page='contacto')


if __name__ == '__main__':
    app.run(debug=True)
