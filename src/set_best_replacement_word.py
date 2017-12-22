from check_candidate_type import is_candidate_type


def set_best_replacement_word(all_tokens_of_all_sentences):
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
                                break
                    else:
                        token.replaced_word = lang_rep
                        break
