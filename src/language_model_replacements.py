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
                try:
                    replacement_words_and_probs = []
                    for similar_word_and_prob in self.model.similar_by_word(
                            token.word_without_punctuations):
                        if similar_word_and_prob[0] != token.word_without_punctuations:
                            replacement_words_and_probs.append(similar_word_and_prob)

                    if replacement_words_and_probs:
                        token.replacements_langmod_and_prob = replacement_words_and_probs
                except KeyError:
                    pass


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
