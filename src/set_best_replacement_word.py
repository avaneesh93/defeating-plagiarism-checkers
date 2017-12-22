from check_candidate_type import is_candidate_type


def set_best_replacement_word(all_tokens_of_all_sentences, replacements_to_do):
    replacement_count = 0

    for sentence in all_tokens_of_all_sentences:
        for token in sentence:
            if not is_candidate_type(token.pos):
                continue

            if token.replacements_langmod_and_prob:
                for lang_rep, _ in token.replacements_langmod_and_prob:
                    if token.replacements_logreg:
                        for logreg_rep in token.replacements_logreg:
                            if lang_rep == logreg_rep:
                                token.replaced_word = lang_rep
                                print('Replacing %s with %s -- 1' % (token.original_word,
                                                                     token.replaced_word))
                                replacement_count += 1

                                token.replacements_langmod_and_prob = None
                                token.replacements_logreg = None

                                if replacement_count >= replacements_to_do:
                                    return

                                break
                    else:
                        token.replaced_word = lang_rep
                        print('Replacing %s with %s -- 2' % (token.original_word,
                                                             token.replaced_word))
                        replacement_count += 1

                        token.replacements_langmod_and_prob = None

                        if replacement_count >= replacements_to_do:
                            return

                        break
