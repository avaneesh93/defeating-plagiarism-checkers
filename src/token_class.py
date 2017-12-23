class Token:
    original_word = None
    replaced_word = None
    word_without_punctuations = None
    is_stopword = None
    pos = None
    lm_probability = None
    replacements_logreg = None
    replacements_langmod = None

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))

        return ', '.join(sb)

    def __repr__(self):
        return self.__str__()
