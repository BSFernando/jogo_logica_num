import flask
from flask import render_template, session, Flask, request
import jogo_treino
import webbrowser
from threading import Timer 

app = Flask(__name__, static_folder = 'templates/static/')

@app.route('/')

def inicial():
    
    return render_template('inicial.html', numbe = 4)

@app.route('/resposta', methods = ['POST'])

def jogar():

    lista = request.form.getlist('valores')
    lista_ordem = [int(lista[0]), int(lista[7]), int(lista[2]), int(lista[5]), 
                int(lista[1]), int(lista[4]), int(lista[3]), int(lista[6])]
    resposta = jogo_treino.Jogando()
    resposta.jogada(lista_ordem)
    valor = resposta.resposta

    if valor <= 0.3 and valor != 0:
        return render_template('inicial.html', numbe = 1)
    elif valor <= 0.6 and valor != 0:
        return render_template('inicial.html', numbe = 2)
    elif valor <= 1 and valor != 0:
        return render_template('inicial.html', numbe = 3) 
    else:
        return render_template('resposta.html') 

    

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(host = '127.0.0.1')