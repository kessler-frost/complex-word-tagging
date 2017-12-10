import pickle
import trained_models as models
import numpy as np
import get_features as gf
from collections import Counter
# from sklearn.metrics import accuracy_score
import warnings
# complex     - 1
# non-complex - 2

output = open("output.txt", "w", encoding="utf-8")

complex_words, non_complex_words = [], []

with open("complex_words_lexicon.pkl", "rb") as f:
    complex_words = pickle.load(f)

with open("non_complex_words_lexicon.pkl", "rb") as g:
    non_complex_words = pickle.load(g)


def supervised(word):

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    labels = []
    labels.append(models.GNB(np.array(gf.get_features(word))))
    labels.append(models.BNB(np.array(gf.get_features(word))))
    labels.append(models.MNB(np.array(gf.get_features(word))))
    labels.append(models.SGDC(np.array(gf.get_features(word))))
    labels.append(models.LRC(np.array(gf.get_features(word))))
    labels.append(models.LSVC(np.array(gf.get_features(word))))
    labels.append(models.NuSVC(np.array(gf.get_features(word))))

    most_common, num_most_common = Counter(labels).most_common(1)[0]
    return most_common


def classifier(word):
    if word in complex_words:
        return 1
    if word in non_complex_words:
        return 2
    return supervised(word)


test_labels = []
test_words = []

# for f in open('test.csv').readlines():
#     word, label = f.strip().split(',')
#     test_labels.append(int(label))
#     test_words.append(word)
#
# pl1 = []
# pl2 = []
# pl3 = []
# pl4 = []
# pl5 = []
# pl6 = []
# pl7 = []
# for tw in test_words:
#
#     pl1.append(models.GNB(np.array(gf.get_features(tw))))
#     pl2.append(models.BNB(np.array(gf.get_features(tw))))
#     pl3.append(models.MNB(np.array(gf.get_features(tw))))
#     pl4.append(models.SGDC(np.array(gf.get_features(tw))))
#     pl5.append(models.LRC(np.array(gf.get_features(tw))))
#     pl6.append(models.LSVC(np.array(gf.get_features(tw))))
#     pl7.append(models.NuSVC(np.array(gf.get_features(tw))))
#
# print(accuracy_score(test_labels, pl1))
# print(accuracy_score(test_labels, pl2))
# print(accuracy_score(test_labels, pl3))
# print(accuracy_score(test_labels, pl4))
# print(accuracy_score(test_labels, pl5))
# print(accuracy_score(test_labels, pl6))
# print(accuracy_score(test_labels, pl7))
