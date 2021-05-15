# Chatbot Tensorflow

[Link para o ChatBot](https://stackoverflow-python-chatbot.herokuapp.com/)

## Como foi desenvolvido?
- Foi realizado o pré-processamento dos textos de perguntas e respostas do Stackoverflow que se encontra no Kaggle utilizando-se de tecnicas de Processamento de Língua Natural (PLN)
- Através da biblioteca de código aberto TensorFlow treinamos a rede neural profunda para encontrar padrões e correlações na base de dados processada
- Salvamos o modelo treinado e criamos uma aplicação web para fazer uso desse modelo e responder a perguntas de maneira inteligente

## Sobre o chatbot
- Foi desenvolvido pelo estudantes de pós-gradução André N. Darcie e Cristiane Lemos para a diciplina de Processamento de Linguagens Naturais no curso de Ciencia de Dados - Aplicada na PUC Minas
- O projeto é de código aberto e seu repositorio pode ser encontrado no Github nesse endereço
- Treinamos apenas uma parte dos dados por questões de custo e tempo, mas o modelo pode ser treinado com o conjunto total de dados

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