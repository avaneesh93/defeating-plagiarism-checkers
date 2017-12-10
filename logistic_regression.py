from sklearn.linear_model import LogisticRegression
import glob
import xml.etree.ElementTree as ET
import string
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle
import os


FILE_DIR_SEMCOR = "./data/semcor"
NONE_WORD = "$"
NONE_SENSE = "#"
encoder = LabelEncoder()


def get_feature(sentence, index):
    feature = defaultdict(float)

    if index < 2:
        feature["-2_%s" % NONE_WORD] += 1.0
    else:
        feature["-2_%s" % sentence[index - 2]] += 1.0

    if index < 1:
        feature["-1_%s" % NONE_WORD] += 1.0
    else:
        feature["-1_%s" % sentence[index - 1]] += 1.0

        feature["0_%s" % sentence[index]] += 1.0

    if index > len(sentence) - 2:
        feature["+1_%s" % NONE_WORD] += 1.0
    else:
        feature["+1_%s" % sentence[index + 1]] += 1.0

    if index > len(sentence) - 3:
        feature["+2_%s" % NONE_WORD] += 1.0
    else:
        feature["+2_%s" % sentence[index + 1]] += 1.0

    return feature


def parse(doc_limit):
    total_doc_count = 0
    sentences = []
    senses_list = []

    for fn in glob.glob(FILE_DIR_SEMCOR + "/" + "*xml"):
        if 0 < doc_limit <= total_doc_count:
            break

        sentence = []
        sense_list = []

        tree = ET.parse(fn)
        root = tree.getroot()
        total_doc_count += 1

        for child in root:
            word = child.attrib['text'].lower()

            if word == ".":
                sentences.append(sentence)
                senses_list.append(sense_list)
                sentence = []
                sense_list = []
                continue

            if word in string.punctuation:
                continue

            if 'sense' in child.attrib:
                sense = child.attrib['sense']
            else:
                sense = NONE_SENSE
            sentence.append(word)
            sense_list.append(sense)

    features = []
    target = []

    for i in range(0, len(sentences)):
        for j in range(0, len(sentences[i])):
            if senses_list[i][j] == NONE_SENSE:
                continue

            feature = get_feature(sentences[i], j)

            features.append(feature)
            target.append(senses_list[i][j])

    return zip(features, target)


def predict_sense(model, sentence, vectorizer):
    features = []

    for j in range(0, len(sentence)):
        feature = get_feature(sentence, j)
        features.append(feature)

    return model.predict(vectorizer.transform(features))


if __name__ == '__main__':
    if os.path.isfile('model.pkl') and os.path.isfile('vectorizer.pkl'):
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
    else :
        labeled_featuresets = parse(150)

        X, y = list(zip(*labeled_featuresets))

        print("---------Transforming features-----------")
        vectorizer = DictVectorizer()
        X = vectorizer.fit_transform(X)
        print("---------Transformed features-----------")

        model = LogisticRegression()
        model.fit(X, y)

        print(model.score(X, y))
        with open('model.pkl', 'wb') as f:
            pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
        with open('vectorizer.pkl', 'wb') as f:
            pickle.dump(vectorizer, f, pickle.HIGHEST_PROTOCOL)

    print(predict_sense(model, ["I", "go", "to", "the", "bank"], vectorizer))
