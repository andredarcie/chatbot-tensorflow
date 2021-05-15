# Chatbot Tensorflow

## Instalação

Utilize o geranciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar a aplicação.

```bash
pip install -U -r requirements.txt
```

## Execução

Para treinar ou carregar a rede neural:
>  Verificar a variavel "modo_treino" em que True é para treinar e salvar a rede neural e False é apenas para carregar a rede neural já salva.
```bash
python chatBotModel.py
```

Para executar o chatbot:
```bash
set FLASK_APP=app.py
flask run
```
Acesse o endereço [localhost](http://localhost:5000) para executar a aplicação.

## Deploy automatizado no Heroku

Toda vez que é feita uma alteração na branch master, o deploy é realizado com as mudanças.

Para verificar os logs em caso de erro:   
```bash
heroku logs --tail --app stackoverflow-python-chatbot
```

## Contribuição
Contribuiçoes serão bem-vindas via pull requests. Tenha certeza que os teste foram feitos

## License
[MIT](https://choosealicense.com/licenses/mit/)