from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Devuelve la página principal de Inicio de la web"""
    return render_template('index.html')


@app.route('/actividades')
def actividades():
    """Devuelve la página de actividades de la web"""
    return render_template('actividades.html')


@app.route('/gastronomia')
def gastronomia():
    """Devuelve la página de gastronomía de la web"""
    return render_template('gastronomia.html')


@app.route('/cultura')
def cultura():
    """Devuelve la página de cultura de la web"""
    return render_template('cultura.html')


@app.route('/idioma')
def idioma():
    """Devuelve la página de idioma de la web"""
    return render_template('idioma.html')


@app.route('/contacto')
def contacto():
    """Devuelve la página de contacto de la web"""
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)
