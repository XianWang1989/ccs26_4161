
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Defining the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}}
    ENTITY: {<NN.*>}
"""

# Creating a chunk parser
chunk_parser = RegexpParser(grammar)

# Parsing the tagged words
parsed_tree = chunk_parser.parse(tagged)

# Display the parse tree
print(parsed_tree)

# Visualizing the parse tree
parsed_tree.pretty_print()
