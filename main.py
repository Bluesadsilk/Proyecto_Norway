from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/actividades')
def actividades():
    return render_template('actividades.html')


@app.route('/gastronomia')
def gastronomia():
    return render_template('gastronomia.html')


@app.route('/cultura')
def cultura():
    return render_template('cultura.html')


@app.route('/idioma')
def idioma():
    return render_template('idioma.html')


if __name__ == '__main__':
    app.run(debug=True)
