from __future__ import division

import glob
import math
import xml.etree.ElementTree as ET
from collections import defaultdict

from sense_mapping import *

FILE_DIR_SEMCOR = "./data/semcor"
FILE_DIR_MASC = "./data/masc"
SENSE_MAP1 = "./data/manual_map.txt"
SENSE_MAP2 = "./data/algorithmic_map.txt"


def parse():
    total_doc_count = 0
    sense_count = defaultdict(int)
    word_counts = {}
    total_word_count_sense = 0
    total_word_count = 0

    for fn in glob.glob(FILE_DIR_SEMCOR + "/" + "*xml"):
        tree = ET.parse(fn)
        root = tree.getroot()
        total_doc_count += 1
        for child in root:
            total_word_count += 1

            if 'sense' in child.attrib:
                if 'pos' not in child.attrib:
                    print("Fail")
                word = child.attrib['text'].lower()
                sense = child.attrib['sense']
                total_word_count_sense += 1
                if word in word_counts:
                    word_counts[word][sense] += 1
                else:
                    word_counts[word] = defaultdict(int)
                    word_counts[word][sense] = 1
                sense_count[sense] += 1

    for fn in glob.iglob(FILE_DIR_MASC + "/**/" + "*xml", recursive=True):
        tree = ET.parse(fn)
        root = tree.getroot()
        total_doc_count += 1
        for child in root:
            total_word_count += 1
            if 'sense' in child.attrib:
                if 'pos' not in child.attrib:
                    print("Fail")
                word = child.attrib['text'].lower()
                sense = child.attrib['sense']
                total_word_count_sense += 1
                if word in word_counts:
                    word_counts[word][sense] += 1
                else:
                    word_counts[word] = defaultdict(int)
                    word_counts[word][sense] = 1
                sense_count[sense] += 1

    # print(sense_count)

    return sense_count, word_counts


if __name__ == '__main__':
    sense_count, word_counts = parse()
    sense_map = parse_sense_mapping(SENSE_MAP1)
    sense_map.update(parse_sense_mapping(SENSE_MAP2))

    input_word = "big"
    pseudo_count = 1
    max = float('-inf')
    max_sense = None

    if input_word not in word_counts:
        print("Wut")
        exit(1)

    total_sense_count = sum(sense_count.values())

    for sense in sense_count.keys():
        p_word_sense = word_counts[input_word].get(sense, pseudo_count) / sum(
            word_counts[input_word].values())
        p_sense = sense_count[sense] / total_sense_count

        val = math.log(p_word_sense) + math.log(p_sense)
        if max < val:
            max = val
            max_sense = sense

    print("Sense = {}".format(max_sense))
    print("WordNet sense = {}".format(sense_map.get(max_sense, None)))
