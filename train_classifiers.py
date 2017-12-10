import pickle
import numpy as np
import time

# NAIVE BAYED MODELS
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

# LINEAR MODELS
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier

# SUPPORT VECTOR MACHINES
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC

with open("train_features.pkl", "rb") as f:
    train_features = pickle.load(f)

train_labels = []
for line in open("train_label.txt").read().split("\n")[:-1]:
    try:
        train_labels.append(int(line))
    except IndexError:
        pass

X = np.array(train_features[:2800])
Y = np.array(train_labels[:2800])

GNB = GaussianNB()
BNB = BernoulliNB()
MNB = MultinomialNB()

LRC = LogisticRegression()
SGDC = SGDClassifier()

LSVC = LinearSVC()
NUSVC = NuSVC(nu=0.05)


startTime = time.time()

GNB = GNB.fit(X, Y)
moGNB = open("moGNB.pkl", "wb")
pickle.dump(GNB, moGNB)
moGNB.close()
print("GNB training completed.")

BNB = BNB.fit(X, Y)
moBNB = open("moBNB.pkl", "wb")
pickle.dump(BNB, moBNB)
moBNB.close()
print("BNB training completed.")

MNB = MNB.fit(X, Y)
moMNB = open("moMNB.pkl", "wb")
pickle.dump(MNB, moMNB)
moMNB.close()
print("MNB training completed.")

LRC = LRC.fit(X, Y)
moLRC = open("moLRC.pkl", "wb")
pickle.dump(LRC, moLRC)
moLRC.close()
print("LRC training completed.")

SGDC = SGDC.fit(X, Y)
moSGDC = open("moSGDC.pkl", "wb")
pickle.dump(SGDC, moSGDC)
moSGDC.close()
print("SGDC training completed.")

LSVC = LSVC.fit(X, Y)
moLSVC = open("moLSVC.pkl", "wb")
pickle.dump(LSVC, moLSVC)
moLSVC.close()
print("LSVC training completed.")

NUSVC = NUSVC.fit(X, Y)
moNUSVC = open("moNUSVC.pkl", "wb")
pickle.dump(NUSVC, moNUSVC)
moNUSVC.close()
print("NUSVC training completed.")

print("time taken =  %s seconds" % (time.time() - startTime))







# CODE TO MAKE TEST LABEL FILE
# label = open("train_label.txt", "w", encoding="utf-8")
# for x in range(1400):
#     label.write(str(1) + "\n")
#
# for x in range(1400):
#     label.write(str(2) + "\n")
#
# label.close()
#
# CODE TO PICKLE FEATURES
# import get_features as gf
#
# features = []
#
# for word in open("train_data.txt", encoding="utf-8").read().split("\n")[:-1]:
#     features.append(gf.get_features(word.strip()))
#
# for fe in features:
#     print(fe)
# print(len(features))
#
# with open("train_features.pkl", "wb") as f:
#     pickle.dump(features, f)
#
# f.close()
