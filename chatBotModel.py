import json
import random
import tensorflow as tf
import tflearn
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open('data.json') as json_data:
    data = json.load(json_data)


palavras = []
classes = []
documentos = []
palavras_ignoradas = stopwords.words('portuguese')
modelo = None
print(palavras_ignoradas)

for questao in data['questoes']:
    for padrao in questao['padroes']:
        palavra = nltk.word_tokenize(padrao)
        palavras.extend(palavra)
        documentos.append((palavra, questao['tag']))

        if questao['tag'] not in classes:
            classes.append(questao['tag'])

# Remove as palavras ignoradas da lista de palavras e pega a raiz de cada palavra
palavras = [stemmer.stem(palavra.lower())
            for palavra in palavras if palavra not in palavras_ignoradas]
palavras = sorted(list(set(palavras)))

print("Chatbot Tensorflow")
print(len(documentos), "documentos", documentos)
print(len(classes), "classes", classes)
print(len(palavras), "raizes das palavras", palavras)

treinamento = []
output = []
output_vazio = [0] * len(classes)

for documento in documentos:
    bolsa_de_palavras = []
    palavras_padrao = documento[0]
    palavras_padrao = [stemmer.stem(palavra.lower())
                       for palavra in palavras_padrao]
    for palavra in palavras:
        bolsa_de_palavras.append(
            1) if palavra in palavras_padrao else bolsa_de_palavras.append(0)

    output_linha = list(output_vazio)
    output_linha[classes.index(documento[1])] = 1

    treinamento.append([bolsa_de_palavras, output_linha])

print("Treinamento:")
print(treinamento)

# Embaralha os dados de treinamento
random.shuffle(treinamento)
treinamento = np.array(treinamento)

treinamento_x = list(treinamento[:, 0])  # palavras padrão
treinamento_y = list(treinamento[:, 1])  # tags

# Limpa a pilha de gráficos padrão e redefine o gráfico padrão global.
# tf.reset_default_graph()
tf.compat.v1.reset_default_graph()


def cria_rede_neural():
    rede_neural = tflearn.input_data(shape=[None, len(treinamento_x[0])])
    rede_neural = tflearn.fully_connected(rede_neural, 8)
    rede_neural = tflearn.fully_connected(rede_neural, 8)
    rede_neural = tflearn.fully_connected(
        rede_neural, len(treinamento_y[0]), activation='softmax')
    rede_neural = tflearn.regression(rede_neural)

    # Configurar o tensorboard
    return tflearn.DNN(rede_neural, tensorboard_dir='tflearn_logs')

def treina_rede_neural():
    modelo.fit(treinamento_x, treinamento_y, n_epoch=5000,
               batch_size=8, show_metric=True)

def salva_rede_neural():
    modelo.save('model.tflearn')

def carrega_rede_neural():
    modelo.load('./model.tflearn')

def limpar_frase(frase):
    palavras_da_frase = nltk.word_tokenize(frase)
    palavras_da_frase = [stemmer.stem(palavra.lower())
                         for palavra in palavras_da_frase]
    return palavras_da_frase


def pega_bolsa_de_palavras(frase, palavras, show_details=False):
    palavras_da_frase = limpar_frase(frase)

    bolsa_de_palavras = [0] * len(palavras)
    for palavra_da_frase in palavras_da_frase:
        for index, palavra in enumerate(palavras):
            if palavra == palavra_da_frase:
                bolsa_de_palavras[index] = 1
                if show_details:
                    print("achou na bolsa: ", palavra)

    return(np.array(bolsa_de_palavras))

LIMITE_DE_ERRO = 0.25

def classifica_frase(frase):
    resultados = modelo.predict([pega_bolsa_de_palavras(frase, palavras)])[0]
    resultados = [[i, resultado]
                  for i, resultado in enumerate(resultados) if resultado > LIMITE_DE_ERRO]
    resultados.sort(key=lambda resultado: resultado[1], reverse=True)
    lista_de_resultados = []
    for resultado in resultados:
        lista_de_resultados.append((classes[resultado[0]], resultado[1]))
    return lista_de_resultados

def encontra_resposta(tag_encontrada):
    for questao in data['questoes']:
        if questao['tag'] == tag_encontrada:
            return questao['respostas'][0]

    return 'Não entendi sua pergunta'

modelo = cria_rede_neural()
#treina_rede_neural()
#salva_rede_neural()
carrega_rede_neural()

#while True:
#    pergunta = input("Digite sua pergunta: ")
#    tag_encontrada = classifica_frase(pergunta)[0][0]
#    resposta = encontra_resposta(tag_encontrada)
#    print(resposta)
