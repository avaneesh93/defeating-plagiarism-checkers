import glob
import string
import xml.etree.ElementTree as ET
from collections import defaultdict

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import tokenize_paragraph
from get_synonym import *
from pickle_util import *


class LogReg:
    FILE_MODEL_PKL = './../datasets/model.pkl'
    FILE_VECTORIZER_PKL = './../datasets/vectorizer.pkl'
    FILE_DIR_SEMCOR = "./../datasets/semcor"
    NONE_WORD = "$"
    NONE_SENSE = "#"
    encoder = LabelEncoder()

    def __init__(self):
        if os.path.isfile(self.FILE_MODEL_PKL) and os.path.isfile(self.FILE_VECTORIZER_PKL):
            self.model = load(self.FILE_MODEL_PKL)
            self.vectorizer = load(self.FILE_VECTORIZER_PKL)
        else:
            labeled_featuresets = self.parse(-1)

            X, y = list(zip(*labeled_featuresets))

            print("---------Transforming features-----------")
            vectorizer = DictVectorizer()
            X = vectorizer.fit_transform(X)
            print("---------Transformed features-----------")

            # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            model = LogisticRegression()
            model.fit(X, y)

            # print(model.score(X_test, y_test))
            # with open('model.pkl', 'wb') as f:
            #     pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
            save(model, self.FILE_MODEL_PKL)
            self.model = model
            # with open('vectorizer.pkl', 'wb') as f:
            #     pickle.dump(vectorizer, f, pickle.HIGHEST_PROTOCOL)
            save(vectorizer, self.FILE_VECTORIZER_PKL)
            self.vectorizer = vectorizer

    def get_feature(self, sentence, index):
        feature = defaultdict(float)

        if index < 2:
            feature["-2_%s" % self.NONE_WORD] += 1.0
        else:
            feature["-2_%s" % sentence[index - 2]] += 1.0

        if index < 1:
            feature["-1_%s" % self.NONE_WORD] += 1.0
        else:
            feature["-1_%s" % sentence[index - 1]] += 1.0

        feature["0_%s" % sentence[index]] += 1.0

        if index > len(sentence) - 2:
            feature["+1_%s" % self.NONE_WORD] += 1.0
        else:
            feature["+1_%s" % sentence[index + 1]] += 1.0

        if index > len(sentence) - 3:
            feature["+2_%s" % self.NONE_WORD] += 1.0
        else:
            feature["+2_%s" % sentence[index + 1]] += 1.0

        return feature

    def parse(self, doc_limit):
        total_doc_count = 0
        sentences = []
        senses_list = []

        for fn in glob.glob(self.FILE_DIR_SEMCOR + "/" + "*xml"):
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
                    sense = self.NONE_SENSE
                sentence.append(word)
                sense_list.append(sense)

        features = []
        target = []

        for i in range(0, len(sentences)):
            for j in range(0, len(sentences[i])):
                if senses_list[i][j] == self.NONE_SENSE:
                    continue

                feature = self.get_feature(sentences[i], j)

                features.append(feature)
                target.append(senses_list[i][j])

        return zip(features, target)

    def predict_sense(self, sentence):
        features = []

        for j in range(0, len(sentence)):
            feature = self.get_feature(sentence, j)
            features.append(feature)

        return self.model.predict(self.vectorizer.transform(features))

    def set_replacements_in_tokens(self, all_tokens_of_all_sentences):
        for sent_index, sentence in enumerate(all_tokens_of_all_sentences):

            # Build a list of only tokens (without punctuations)
            tokens_of_sentence = [token.word_without_punctuations for token in sentence]

            senses = self.predict_sense(tokens_of_sentence)

            for token_index in range(len(sentence)):
                new_words = []
                pos_names = list(get_synonym(senses[token_index]))
                if len(pos_names) == 0:
                    continue

                for pos, names in pos_names:
                    if pos == 'a':
                        for name in names:
                            if name != tokens_of_sentence[token_index]:
                                new_words.append(name)

                    if new_words:
                        sentence[token_index].replacements_logreg = new_words


if __name__ == '__main__':
    paragraph = open('./../datasets/test.txt', encoding='utf8').read()

    all_tokens_of_all_sentences = tokenize_paragraph.tokenize(paragraph)

    log_reg = LogReg()

    log_reg.set_replacements_in_tokens(all_tokens_of_all_sentences)

    for sentence in all_tokens_of_all_sentences:
        for token in sentence:
            print(token)
