from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal (index)
@app.route('/')
def inicio():
    return render_template('index.html')  # Renderiza el archivo HTML principal

# Rutas para otros índices
@app.route('/index1')
def index1():
    return render_template('index1.html')  # Renderiza el archivo HTML index1

@app.route('/index2')
def index2():
    return render_template('index2.html')  # Renderiza el archivo HTML index2

@app.route('/index3')
def index3():
    return render_template('index3.html')  # Renderiza el archivo HTML index3

@app.route('/index4')
def index4():
    return render_template('index4.html')  # Renderiza el archivo HTML index4

@app.route('/index5')
def index5():
    return render_template('index5.html')  # Renderiza el archivo HTML index5

@app.route('/index6')
def index6():
    return render_template('index6.html')  # Renderiza el archivo HTML index6

@app.route('/index7')
def index7():
    return render_template('index7.html')  # Renderiza el archivo HTML index7

@app.route('/index8')
def index8():
    return render_template('index8.html')  # Renderiza el archivo HTML index8

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
