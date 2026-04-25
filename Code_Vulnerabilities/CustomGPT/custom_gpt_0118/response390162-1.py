
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar with multiple clauses
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media (e.g., adventure movies)
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}               # Relation (e.g., featuring performances)
  ENTITY: {<NN.*>}                                 # Entity (e.g., daniel craig)
  PP: {<IN><MEDIA|ENTITY>}                         # Prepositional phrase
  VP: {<V.*><MEDIA|ENTITY|PP>*}                    # Verb phrase
  CLAUSE: {<MEDIA|ENTITY><VP>}                     # Full clause
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
result = chunk_parser.parse(tagged)

# Print the result
print(result)
result.draw()  # To visualize the chunks
