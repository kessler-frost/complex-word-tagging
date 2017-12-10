from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk import ngrams
import pickle


# function used in character level bigram and trigram
def get_character_ngrams(word, n):
    return ["".join(gram) for gram in ngrams(word, n)]


# # length
# def fe01(word):
#     return int(len(word))


# syllable count
def fe02(word):
    count = 0
    vowels = 'aeiouy'
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return int(count)


# synset count
def fe03(word):
    return int(len(wn.synsets(word)))


# word to stem ratio
def fe04(word):
    stemmer = PorterStemmer()
    return int(len(word)/len(stemmer.stem(word)))


# synonyms count
def fe05(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return len(set(synonyms))


# hypernym count
def fe06(word):
    count = 0
    for synset in wordnet.synsets(word):
        for hypernym in synset.hypernyms():
            count += 1
    return int(count)


# bigram count
def fe07(word):
    with open("character_bigram.pkl", "rb") as f:
        character_bigram = pickle.load(f)
    score = 0
    for gram in get_character_ngrams(word, 2):
        try:
            score += character_bigram[gram]
        except KeyError:
            score += 0
    return int(score / len(word))


# trigram count
def fe08(word):
    with open("character_trigram.pkl", "rb") as g:
        character_trigram = pickle.load(g)
    score = 0
    for gram in get_character_ngrams(word, 3):
        try:
            score += character_trigram[gram]
        except KeyError:
            score += 0
    return int(score / len(word))


def get_features(word):
    features = []
    # features.append(fe01(word))
    features.append(fe02(word))
    features.append(fe03(word))
    features.append(fe04(word))
    features.append(fe05(word))
    features.append(fe06(word))
    features.append(fe07(word))
    features.append(fe08(word))

    return features
