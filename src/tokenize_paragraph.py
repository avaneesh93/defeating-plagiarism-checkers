from nltk.corpus import gutenberg
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer

ABBREVIATIONS = ['dr', 'mrs']


def get_training_text():
    text = ""

    for file_id in gutenberg.fileids():
        text += gutenberg.raw(file_id)

    return text


def get_tokenizer(training_text):
    trainer = PunktTrainer()
    trainer.INCLUDE_ALL_COLLOCS = True
    trainer.train(training_text)
    tokenizer = PunktSentenceTokenizer(trainer.get_params())
    tokenizer._params.abbrev_types.update(ABBREVIATIONS)

    return tokenizer


def tokenize(paragraph):
    training_text = get_training_text()
    tokenizer = get_tokenizer(training_text)
    sentences = [s for s in tokenizer.tokenize(paragraph) if s is not None]

    words = {}

    for index, sent in enumerate(sentences):
        words[index] = sent.split()

    print(words)
