
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)
