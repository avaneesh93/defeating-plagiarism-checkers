from check_candidate_type import is_candidate_pos_type


def set_best_replacement_word(all_tokens_of_all_sentences, replacements_to_do):
    replacement_count = 0

    for sentence in all_tokens_of_all_sentences:
        for token in sentence:
            if not is_candidate_pos_type(token.pos):
                continue

            if token.replacements_langmod:
                for lang_rep in token.replacements_langmod:
                    if token.replacements_logreg and \
                                    len(
                                        intersect(token.replacements_langmod,
                                                  token.replacements_logreg)
                                    ) > 0:
                        for logreg_rep in token.replacements_logreg:
                            if lang_rep == logreg_rep:
                                token.replaced_word = lang_rep
                                print('Replacing %s with %s -- 1' % (token.original_word,
                                                                     token.replaced_word))
                                replacement_count += 1

                                token.replacements_langmod = None
                                token.replacements_logreg = None

                                if replacement_count >= replacements_to_do:
                                    return

                                break
                    else:
                        token.replaced_word = lang_rep
                        print('Replacing %s with %s -- 2' % (token.original_word,
                                                             token.replaced_word))
                        replacement_count += 1

                        token.replacements_langmod = None

                        if replacement_count >= replacements_to_do:
                            return

                        break


def intersect(a, b):
    return list(set(a) & set(b))
