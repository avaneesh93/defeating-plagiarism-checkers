from nltk.corpus import wordnet as wn
import pickle
import os


INDEX_PATH = "./data/index.sense"
MANUAL_MAP = "./data/manual_map.txt"
ALGO_MAP = "./data/algorithmic_map.txt"


def get_synsets(offsets):
    syns = list(wn.all_synsets())
    offsets_list = [(s.offset(), s) for s in syns]
    offsets_dict = dict(offsets_list)
    return map(lambda off: offsets_dict[off], offsets)


def get_synonym(sense):
    sense_dict = {}
    noad_to_wn = {}

    if os.path.isfile('sense_index.pkl') and os.path.isfile('noad_to_wn.pkl'):
        with open('sense_index.pkl', 'rb') as f:
            sense_dict = pickle.load(f)
        with open('noad_to_wn.pkl', 'rb') as f:
            noad_to_wn = pickle.load(f)
    else:
        with open(INDEX_PATH, 'r') as f:
            for line in f:
                lst = line.split()
                sense_dict[lst[0]] = lst[1]

        with open(MANUAL_MAP, 'r') as f:
            for line in f:
                lst = line.split()
                noad_to_wn[lst[0]] = lst[1].split(',')

        with open(ALGO_MAP, 'r') as f:
            for line in f:
                lst = line.split()
                noad_to_wn[lst[0]] = lst[1].split(',')

        with open('sense_index.pkl', 'wb') as f:
            pickle.dump(sense_dict, f, pickle.HIGHEST_PROTOCOL)
        with open('noad_to_wn.pkl', 'wb') as f:
            pickle.dump(noad_to_wn, f, pickle.HIGHEST_PROTOCOL)

    if sense not in noad_to_wn:
        return []

    wn_senses = noad_to_wn[sense]
    offsets = []
    for wn_sense in wn_senses:
        if ';' not in wn_sense and wn_sense in sense_dict:
            offsets.append(sense_dict[wn_sense])
        else:
            continue
    ss = get_synsets(map(lambda off: int(off), offsets))

    # for s in ss:
    #     print(s)
    #     print(s.pos())
    #     print(s.definition())
    #     print(s.lemma_names())
    #     print()

    return map(lambda sst: (sst.pos(), sst.lemma_names()), ss)


if __name__ == '__main__':
    get_synonym("/dictionary/sense/en_us_NOAD3e_2012/m_en_us1224756.001")