import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random

import json
with open('data.json') as json_data:
    data = json.load(json_data)


palavras = []
classes = []
documentos = []
palavras_ignoradas = ['?']

for questao in data['questoes']:
    for padrao in data['padroes']:
        palavra = nltk.word_tokenize(padrao)
        palavras.extend(palavra)
        documentos.append(palavra, data['tag'])

        if data['tag'] not in classes:
            classes.append(data['tag'])

# Remove as palavras ignoradas da lista de palavras e pega a raiz de cada palavra
palavras = [stemmer.stem(palavra.lower()) for palavra in palavras if palavra not in palavras_ignoradas]