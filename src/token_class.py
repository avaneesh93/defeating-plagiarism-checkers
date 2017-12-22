class Token:
    original_word = None
    word_without_punctuations = None
    is_stopword = None
    pos = None
    lm_probability = None
    replacements_logreg = None
    replacements_langmod = None

    def __str__(self):
        return "Token(original_word=%s, word_without_punctuations=%s, " \
               "is_stopword=%s, pos=%s, lm_probability=%s, replacements_logreg=%s, " \
               "replacements_langmod=%s)" % \
               (self.original_word, self.word_without_punctuations, self.is_stopword, self.pos,
                self.lm_probability, self.replacements_logreg, self.replacements_langmod)
