from gensim.models import KeyedVectors

FILE_FACEBOOK_WORD_VECTORS = './../datasets/wiki.en.vec'


class LanguageModelReplacement:
    model = None

    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format(FILE_FACEBOOK_WORD_VECTORS)

    def set_language_model_replacements(self, all_tokens_of_all_sentences):
        for similar_word in self.model.most_similar_to_given('best', self.model.vocab):
            print(similar_word)


if __name__ == '__main__':
    lmr = LanguageModelReplacement()
    lmr.set_language_model_replacements(None)
