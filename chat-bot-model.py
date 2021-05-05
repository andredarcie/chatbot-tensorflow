import json
import random
import tensorflow as tf
import tflearn
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open('data.json') as json_data:
    data = json.load(json_data)


palavras = []
classes = []
documentos = []
palavras_ignoradas = ['?']

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
