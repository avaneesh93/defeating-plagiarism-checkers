import gensim

import tokenize_paragraph

FILE_FACEBOOK_WORD_VECTORS = './../datasets/wiki.en.vec'


class LanguageModelReplacement:
    model = None

    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(FILE_FACEBOOK_WORD_VECTORS)

    def set_language_model_replacements(self, all_tokens_of_all_sentences):
        for sentence in all_tokens_of_all_sentences:
            for token in sentence:
                for similar_word, _ in self.model.similar_by_word(token.word_without_punctuations):
                    if similar_word != token.word_without_punctuations:
                        token.replaced_word = similar_word
                        break


if __name__ == '__main__':
    paragraph = open('./../datasets/test.txt', encoding='utf8').read()

    all_tokens_of_all_sentences = tokenize_paragraph.tokenize(paragraph)

    lmr = LanguageModelReplacement()
    lmr.set_language_model_replacements(all_tokens_of_all_sentences)

    print(all_tokens_of_all_sentences)

    print('~~~~~~~~~~~~~~~')

    for sentence in all_tokens_of_all_sentences:
        for token in sentence:
            print(token)
