import nltk
from nltk.corpus import gutenberg
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer

from pos import set_parts_of_speech_in_tokens
from remove_punctuations import remove_surrounding_punctuations
from token_class import Token

ABBREVIATIONS = ['dr', 'mrs']


def get_training_text():
    text = ""

    nltk.download('gutenberg')

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


def split_paragraph_into_sentences(paragraph):
    training_text = get_training_text()
    tokenizer = get_tokenizer(training_text)
    return [s for s in tokenizer.tokenize(paragraph) if s is not None]


def tokenize(paragraph):
    nltk.download('stopwords')
    stopwords = set(nltk.corpus.stopwords.words('english'))

    sentences = split_paragraph_into_sentences(paragraph)

    all_tokens_of_all_sentences = []

    for sent_index, sent in enumerate(sentences):
        tokens_in_this_sentence = []

        for word_index, word in enumerate(sent.split()):
            token = Token()
            token.original_word = word
            token.word_without_punctuations = remove_surrounding_punctuations(word).lower()

            if token.word_without_punctuations in stopwords:
                token.is_stopword = True
            else:
                token.is_stopword = False

            tokens_in_this_sentence.append(token)

        all_tokens_of_all_sentences.append(tokens_in_this_sentence)

    set_parts_of_speech_in_tokens(all_tokens_of_all_sentences)

    return all_tokens_of_all_sentences
