
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig who acted in some of the best films directed by various directors."
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*>(directed|acted|featuring)<DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

chunk_parser = RegexpParser(grammar)
parsed_tree = chunk_parser.parse(tagged)

print(parsed_tree)
parsed_tree.pretty_print()
