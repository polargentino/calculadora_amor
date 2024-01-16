from flask import Flask, render_template, request
import random

app = Flask(__name__)

def calculadora_de_amor(nombre1, nombre2):
    nombres_concatenados = (nombre1 + nombre2).lower()
    nombres_concatenados = nombres_concatenados.replace(" ", "")
    porcentaje_amor = random.randint(1, 100)
    return porcentaje_amor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    porcentaje_amor = calculadora_de_amor(nombre1, nombre2)
    return render_template('result.html', nombre1=nombre1, nombre2=nombre2, porcentaje_amor=porcentaje_amor)

if __name__ == '__main__':
    app.run(debug=True)



