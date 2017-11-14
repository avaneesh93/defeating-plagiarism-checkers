from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = "This is the best day of my life."
stopwords = stopwords.words()
tokens = [x for x in word_tokenize(sentence) if x not in stopwords]

print(tokens)
