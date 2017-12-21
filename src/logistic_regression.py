import glob
import string
import xml.etree.ElementTree as ET
from collections import defaultdict

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from get_synonym import *
from pickle_util import *


class LogReg:
    FILE_DIR_SEMCOR = "./data/semcor"
    NONE_WORD = "$"
    NONE_SENSE = "#"
    encoder = LabelEncoder()

    def __init__(self):
        if os.path.isfile('model.pkl') and os.path.isfile('vectorizer.pkl'):
            # with open('model.pkl', 'rb') as f:
            #     model = pickle.load(f)
            self.model = load('model.pkl')
            # with open('vectorizer.pkl', 'rb') as f:
            #     vectorizer = pickle.load(f)
            self.vectorizer = load('vectorizer.pkl')
        else:
            labeled_featuresets = self.parse(-1)

            X, y = list(zip(*labeled_featuresets))

            print("---------Transforming features-----------")
            vectorizer = DictVectorizer()
            X = vectorizer.fit_transform(X)
            print("---------Transformed features-----------")

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            model = LogisticRegression()
            model.fit(X_train, y_train)

            print(model.score(X_test, y_test))
            # with open('model.pkl', 'wb') as f:
            #     pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
            save(model, 'model.pkl')
            self.model = model
            # with open('vectorizer.pkl', 'wb') as f:
            #     pickle.dump(vectorizer, f, pickle.HIGHEST_PROTOCOL)
            save(vectorizer, 'vectorizer.pkl')
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

    def get_replacements(self, sentences):
        replacements = {}

        for k in range(0, len(sentences)):
            sentence = sentences[k]
            sentence_list = sentence.split()
            sentence_list[-1] = sentence_list[-1].rstrip('.')
            senses = self.predict_sense(sentence_list)

            # p_init = detect_plagiarism(sentence)
            sentence_map = {}
            # print("----------")

            for i in range(0, len(senses)):
                new_words = []
                pos_names = list(get_synonym(senses[i]))
                if len(pos_names) == 0:
                    continue
                for pos, names in pos_names:
                    if pos == 'a':
                        old_word = sentence_list[i]
                        for name in names:
                            if not name == old_word:
                                new_words.append(name)

                    if new_words:
                        sentence_map[i] = new_words

            if len(sentence_map) > 0:
                replacements[k] = sentence_map

                # print(sentence_list)
                # sentence_list[-1] = sentence_list[-1] + "."
                # p_fin = detect_plagiarism(' '.join(sentence_list))
                # total_p += p_init - p_fin

        # print("AVG = {}".format(total_p/100))
        return replacements
        # for sense in senses:
        #     get_synonym(sense)
        #     print("-----------")


if __name__ == '__main__':
    os.chdir('..')
    os.chdir('datasets')

    with open("test.txt") as f:
        first_n_lines = f.readlines()[0:10]

    log_reg = LogReg()
    print(log_reg.get_replacements(first_n_lines))
