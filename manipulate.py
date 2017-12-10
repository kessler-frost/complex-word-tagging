# # http://www.talkenglish.com/vocabulary/top-2000-vocabulary.aspx
#
# from nltk.tokenize import word_tokenize
#
# from nltk import ngrams
# import pickle
#
# def get_character_ngrams(word, n):
#     return ["".join(gram) for gram in ngrams(word, n)]
# #
# # x = open("store.txt", "w",encoding="utf-8")
# #
# # words = []
# #
# # for word in open("train_words_complex.txt").read().split("\n")[:-1]:
# #     words.append(word.strip())
# #
# # for word in open("train_words_simple.txt").read().split("\n")[:-1]:
# #     words.append(word.strip())
# #
# # print(words)
# #
# # bigrams = []
# #
# # for word in words:
# #     for gram in get_character_ngrams(word, 3):
# #         bigrams.append(gram)
# #
# # bigram_dict = {i:bigrams.count(i) for i in set(bigrams)}
# #
# # print(bigrams)
# #
# # with open("character_trigram.pkl", "wb") as f:
# #     pickle.dump(bigram_dict, f)
# #
# # f.close()
# #
# #
# #
# #
# # x.close()
#
#
# def get_bigram(word):
#     with open("character_bigram.pkl", "rb") as f:
#         character_bigram = pickle.load(f)
#     score = 0
#     for gram in get_character_ngrams(word, 2):
#         score += character_bigram[gram]
#         print(gram)
#     return int (score / len(word))


import pickle

complex_words = []

for word in open("complex_words_lexicon.txt").read().split("\n")[:-1]:
    complex_words.append(word.strip())

with open("complex_words_lexicon.pkl", "wb") as f:
    pickle.dump(complex_words, f)


non_complex_words = []

for word in open("non_complex_words_lexicon.txt").read().split("\n")[:-1]:
    non_complex_words.append(word.strip())

with open("non_complex_words_lexicon.pkl", "wb") as g:
    pickle.dump(non_complex_words, g)

f.close()
g.close()
