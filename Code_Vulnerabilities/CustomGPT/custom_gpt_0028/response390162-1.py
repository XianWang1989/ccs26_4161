
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by some director"

# Tokenizing and POS tagging the phrase
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                      # Noun phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}              # Verbs followed by a noun phrase
  ENTITY: {<NN.*>}                                # Entities
  DIRECTOR: {<V.*>{<IN><NP>} }                    # Specific structure for directors
"""

# Create a RegexpParser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Display the chunked output
print(chunked)

# Draw the tree (optional)
chunked.draw()
