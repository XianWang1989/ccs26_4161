import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunk grammar
grammar = r"""
    MEDIA: {<JJ>*<NN.*>+}                  # Nouns, with optional adjectives
    YEAR: {<CD>}                           # Years as cardinal numbers
    RANGE: {<IN><YEAR><CC><YEAR>}         # e.g., between 2000 and 2015
    ENTITY: {<NNP>+}                       # Proper nouns (like names)
    ACTION: {<VBG>}                        # Verbs in -ing form (e.g., featuring)
    RELATION: {<ACTION><MEDIA>}           # e.g., featuring performances
    FULL: {<MEDIA><RANGE>?<RELATION><IN><ENTITY>} # full structure
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the sentence
tree = chunk_parser.parse(tagged)

# Print the result
tree.pretty_print()
