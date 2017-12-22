from remove_punctuations import PUNCTUATIONS, remove_surrounding_punctuations


def restore_case(replaced_word, original_word):
    if original_word and replaced_word:
        if original_word.istitle():
            replaced_word = replaced_word.title()

    return replaced_word


def restore_punctuations(replaced_word, original_word):
    start_index = 0
    while start_index < len(original_word) and original_word[start_index] in PUNCTUATIONS:
        replaced_word = original_word[start_index] + replaced_word
        start_index += 1

    end_index = len(original_word) - 1
    while end_index >= 0 and original_word[end_index] in PUNCTUATIONS:
        replaced_word = replaced_word + original_word[end_index]
        end_index -= 1

    return replaced_word


def generate_output_text_from_tokens(all_tokens_of_all_sentences):
    output_text = ""

    for sentence in all_tokens_of_all_sentences:
        for token in sentence:
            if token.replaced_word:
                replaced_word = token.replaced_word
                replaced_word = restore_case(replaced_word,
                                             remove_surrounding_punctuations(token.original_word))
                replaced_word = restore_punctuations(replaced_word, token.original_word)

                output_text += replaced_word

            elif token.original_word:
                output_text += token.original_word

    return output_text


if __name__ == '__main__':
    rep = "excellent"
    orig = ",Amazing."

    rep = restore_case(rep, remove_surrounding_punctuations(orig))
    rep = restore_punctuations(rep, orig)

    print(rep)
