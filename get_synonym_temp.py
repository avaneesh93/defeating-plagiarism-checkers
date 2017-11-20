from nltk.corpus import wordnet as wn


def get_synonym(word, pos):
    for ss in wn.synsets(lemma=word, pos=pos):
        print(ss)
        print(ss.definition())
        print(ss.lemma_names())
        print()


if __name__ == '__main__':
    get_synonym('smart', wn.ADJ)
