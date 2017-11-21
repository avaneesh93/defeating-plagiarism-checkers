from __future__ import division
from naive_bayes import naive_bayes, FILE_DIR_MASC, parse
import glob
import xml.etree.ElementTree as ET


def check_accuracy():
    sense_count, word_counts = parse(312)
    filenames = glob.glob(FILE_DIR_MASC + "/**/" + "*xml", recursive=True)

    total = 0
    total_correct = 0

    print(len(filenames))

    for i in range(313, len(filenames)):
        fn = filenames[i]
        tree = ET.parse(fn)
        root = tree.getroot()
        for child in root:
            if 'sense' in child.attrib:
                if 'pos' not in child.attrib:
                    print("Fail")
                word = child.attrib['text'].lower()
                correct_sense = child.attrib['sense']
                try:
                    expected_sense = naive_bayes(word, sense_count, word_counts)
                except ValueError as e:
                    continue

                if correct_sense == expected_sense:
                    total_correct += 1
                total += 1

    print("Accuracy = {}".format(total_correct/total))


if __name__ == '__main__':
    check_accuracy()
