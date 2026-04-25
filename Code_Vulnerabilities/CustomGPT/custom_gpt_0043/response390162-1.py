
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig who acted in some of the best films directed by various directors."

# Tokenizing and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Defining the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
parsed_tree = chunk_parser.parse(tagged)

# Printing the result
print(parsed_tree)

# Optionally: Visualize the chunked tree
parsed_tree.pretty_print()
