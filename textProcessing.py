import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stemming(word):
    return stemmer.stem(word.lower())

def wordBag(tokenizeSentence, allWords):
    tokenizeWords = [stemming(w) for w in tokenizeSentence]
    bag = np.zeros(len(allWords), dtype=np.float32)
    for idx, w in enumerate(allWords):
        if w in  tokenizeWords:
            bag[idx] = 1.0
    return bag