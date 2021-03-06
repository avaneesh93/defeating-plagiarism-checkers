import nltk


def set_parts_of_speech_in_tokens(all_tokens_of_all_sentences):
    nltk.download('averaged_perceptron_tagger')

    for sentence in all_tokens_of_all_sentences:
        for token in sentence:
            _, token.pos = nltk.pos_tag([token.word_without_punctuations])[0]
