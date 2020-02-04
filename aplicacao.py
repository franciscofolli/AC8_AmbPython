from flask import Flask, render_template
from flask import request #importa funções de parâmetros para request
import form
# notações de variáveis
#f --> função
#c --> caracter/string
#ft --> float
#a --> array
#li --> lista 

app = Flask(__name__) #Instância para que o Flask funcione / Objeto
#caso criar uma pasta especifica para templates, adicionar virgula e a função 
#template_folder = "nome da pasta"
#ex: app = Flask(__name__, template_folder = 'pãotemplates')


#Pagina inicial
@app.route('/', methods = ['GET', 'POST']) # Define Rotas para serem executadas / Embrulho --> descorador --> Wrap
def index():
    return render_template('index.html')


@app.route('/cursos', methods = ['GET', 'POST'])
def curs():
    return render_template('cursos.html')

#page detalhes dos cursos/faculdade
@app.route('/detalhes', methods = ['GET', 'POST'])
def detalhes():
    return render_template('detalhes.html')

#page disciplinas
@app.route('/disciplinas', methods = ['GET', 'POST'])
def disciplinas():
    return render_template('disciplinas.html')
#page noticias
@app.route('/noticias', methods = ['GET', 'POST'])
def noticias():
    return render_template('noticias.html')

@app.route('/testeparam', methods = ['GET', 'POST']) #parametros simples com ? separando da rota
def param():
    nome = request.args.get('param1', 'não há valor neste parâmetro')
    email = request.args.get('param2', 'não há valor neste parâmetro')
    return f"o Parâmetro é {nome} e {email} "

#@app.route('/param/') #rota alternativa caso não seja informado valor
#@app.route('/param/<nome>/') #informar rota e o parâmetro junto separando por slash e sempre colocando mais uma na frente
#@app.route('/param/<nome>/<sobrenome>/') #adicionar mais parâmetros com mais rotas, assim acrescentando também o parâmetro
@app.route('/param2', methods = ['GET', 'POST'])#para validar um tipo de valor, como inteiro, coloque o tipo seguido por :
def param2():
    title = 'Curso Flask'
    comentario = form.Comentario(request.form)
    print (comentario.nome.data)
    print (comentario.idade.data)
    print (comentario.email.data)
    print (comentario.comentario.data)
    return render_template('python_tags.html', form=comentario, title = title)
    # render_template('python_tags.html', nome=nome, sobrenome=sobrenome, idade=idade, lista=litswx, form=comentario)


app.run(debug = 'true') # Executa o servidor por padrão na porta 5000

#app.run(debug = false | true, port = <informa porta personalizada>)



#Funções do Flask

#return render_template('python_tags.html', nome=nome, sobrenome=sobrenome, idade=idade)
#quando colocas-se variaveis nessa função é possivel chamar as variaveis no html utilizando {{ <nome da variavel> }}
#que devera ser definida na chamada da função, conforme abaixo.
#return render_template('nomedo.html', variavelparahtml=varpython, variavelparahtml=varpython, variavelparahtml=varpython)

#Request para criação de parâmetros.

#request.args.get('<nome da variavel>','<valor padrão caso não seja recebido valor na variável>')

#quando representado na url ficará por: /rota?<nome do parâmetro>='valor passado'

#ex: http://localhost:5000/testeparam?param1=Zeca%20Homem

#acrescentando chamadas de funções é possivel RETORNAR a quantidade de parâmetros maior, veja:

# @app.route('/testeparam')
# def param():
#     parametro = request.args.get('param1', 'não há valor neste parâmetro')
#     parametro2 = request.args.get('param2', 'não há valor neste parâmetro')
#     return f"o Parâmetro é {parametro} e {parametro2} "