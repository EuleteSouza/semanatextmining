# biblioteca do google de texto-voz
from gtts import gTTS
# biblioteca flask, render template - renderizar a pagina web
from flask import Flask, render_template,request
import os

# criando o objeto flask
app = Flask(__name__)
# / - página principal
# POST - INSERIR
# GET - RECUPERAR

@app.route('/',methods=['GET','POST'])
def index():
    audio_path = None
    if request.method == 'POST':
        # pegar valor do html<textfield>
        texto = request.form['texto']
        # configurar o idioma
        lingua = 'pt-br'
        # Criação do objeto
        tts = gTTS(text=texto,lang=lingua)
        # Nome do arquivo de áudio
        audio_path = "static/audio_exemplo.mp3"
        # Salvar o arquivo
        tts.save(audio_path)
    return render_template('index.html',audio_path=audio_path)

if __name__== '__main__':
    app.run(debug=True)