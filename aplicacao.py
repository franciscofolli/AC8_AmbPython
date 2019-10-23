from flask import Flask, render_template
# notações de variáveis
#f --> função
#c --> caracter/string
#ft --> float
#a --> array
#li --> lista 

app = Flask(__name__)

#Pagina inicial
@app.route('/')
def index():
    return render_template('index.html')

#page cursos
@app.route('/cursos')
def curs():
    return render_template('cursos.html')

#page detalhes dos cursos/faculdade
@app.route('/detalhes')
def detalhes():
    return render_template('detalhes.html')

#page disciplinas
@app.route('/disciplinas')
def detalhes():
    return render_template('disciplinas.html')

#page noticias
@app.route('/noticias')
def detalhes():
    return render_template('noticias.html')

app.run()







