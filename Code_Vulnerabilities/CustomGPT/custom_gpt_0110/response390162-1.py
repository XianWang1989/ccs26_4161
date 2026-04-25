
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define your grammar with multiple rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}        # Chunk verbs followed by NP
  ENTITY: {<NN.*>}                          # Chunk single nouns
"""

# Create a RegexpParser with the defined grammar
chunker = RegexpParser(grammar)

# Parse the tagged tokens
result = chunker.parse(tagged)

# Print the result
print(result)

# Draw the chunk tree (optional)
result.draw()
