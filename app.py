from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from chatBotModel import classifica_frase, encontra_resposta

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    mensagem = StringField('Mensagem:', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form   = InputForm(request.form)
    resposta = 'No-response'

    if form.validate_on_submit():
        tag_encontrada = classifica_frase(form.mensagem.data)[0][0]
        resposta = encontra_resposta(tag_encontrada)

    return render_template('index.html', form=form, resposta=resposta)

if __name__ == '__main__':
    app.run()