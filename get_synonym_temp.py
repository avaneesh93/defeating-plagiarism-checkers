from nltk.corpus import wordnet as wn
from nltk.wsd import lesk


def get_sysnset():
    sent1 = ['He', 'is', 'going', 'to', 'stand', 'for', 'office', '.']
    sent2 = ['He', 'is', 'going', 'to', 'the', 'bicycle', 'stand', '.']

    ss1 = lesk(sent1, 'stand')
    ss2 = lesk(sent2, 'stand')

    print(ss1)
    print(ss1.definition())
    print(ss1.lemma_names())

    print(ss2)
    print(ss2.definition())
    print(ss2.lemma_names())


def get_synonym(word, pos):
    for ss in wn.synsets(lemma=word, pos=pos):
        print(ss)
        print(ss.definition())
        print(ss.lemma_names())
        print()


if __name__ == '__main__':
    # get_synonym('smart', wn.ADJ)
    get_sysnset()
