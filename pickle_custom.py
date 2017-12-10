import pickle

words = []
for word in open("non_complex_words_lexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    words.append(word.lower())

with open("non_complex_words_lexicon.pkl", "wb") as f:
    pickle.dump(words, f)

f.close()
