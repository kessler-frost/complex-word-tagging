import pickle


def GNB(features):
    with open("moGNB.pkl", "rb") as f:
        moGNB = pickle.load(f)
    return moGNB.predict(features)[0]


def BNB(features):
    with open("moBNB.pkl", "rb") as f:
        moBNB = pickle.load(f)
    return moBNB.predict(features)[0]


def MNB(features):
    with open("moMNB.pkl", "rb") as f:
        moMNB = pickle.load(f)
    return moMNB.predict(features)[0]


def LRC(features):
    with open("moLRC.pkl", "rb") as f:
        moLRC = pickle.load(f)
    return moLRC.predict(features)[0]


def SGDC(features):
    with open("moSGDC.pkl", "rb") as f:
        moSGDC = pickle.load(f)
    return moSGDC.predict(features)[0]


def LSVC(features):
    with open("moLSVC.pkl", "rb") as f:
        moLSVC = pickle.load(f)
    return moLSVC.predict(features)[0]


def NuSVC(features):
    with open("moNUSVC.pkl", "rb") as f:
        moNUSVC = pickle.load(f)
    return moNUSVC.predict(features)[0]
