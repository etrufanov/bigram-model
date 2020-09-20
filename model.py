import nltk
import pickle
import numpy as np
import requests
from bs4 import BeautifulSoup
nltk.download('punkt')

class TextGenerator:
    def __init__(self):
        self.bigram_dict = {}

    def fit(self, file):
        with open(file) as f:
            text = f.read()

        # разбиение текста на слова
        list_words = nltk.word_tokenize(text)

        # приведение к lowercase
        list_words = list(map(lambda x: x.lower(), list_words))

        # удаление неалфавитных символов и отделение предложений
        alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю.?!'
        list_words = [word for word in list_words if any(alpha in word for alpha in alphabet)]
        i = 0
        list_sentences = []
        while i < len(list_words):
            sentence = []
            while i < len(list_words) and list_words[i] != '.' \
                and list_words[i] != '!' and list_words[i] != '?':
                sentence.append(list_words[i])
                i += 1
            list_sentences.append(sentence)
            i += 1

        # формирование биграмм
        bigram_dict = {}
        for sentence in list_sentences:
            for i in range(len(sentence)-1):
                if sentence[i] not in bigram_dict:
                    bigram_dict[sentence[i]] = []
                bigram_dict[sentence[i]].append(sentence[i+1])
        for word in [*bigram_dict]:
            bigram_dict[word] = list(set(bigram_dict[word]))

        self.bigram_dict = bigram_dict
        return self

    def generate(self, prefix=None):
        if prefix:
            prefix_token = nltk.word_tokenize(prefix)
            prefix_token = list(map(lambda x: x.lower(), prefix_token))
            alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю.?!'
            prefix_token = [word for word in prefix_token if any(alpha in word for alpha in alphabet)]
            start = prefix_token[-1]
        else:
            start = np.random.choice([*self.bigram_dict])
        sentence = prefix + ' ' or ''
        i = 1
        cur = start
        max_len = np.random.choice(np.arange(7,20))
        while self.bigram_dict.get(cur) and i < max_len:
            i += 1
            cur = np.random.choice(self.bigram_dict[cur])
            sentence += (cur + ' ')
        return sentence[:-1]

# model = TextGenerator()
# model.fit('text.txt')
# print('let`s go!')
# while True:
#     text = input()
#     print(model.generate(text))
