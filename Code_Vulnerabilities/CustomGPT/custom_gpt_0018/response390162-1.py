
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# First, tokenize and tag the phrase
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media noun phrases
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}             # Relation including a verb and a media NP
  ENTITY: {<NN.*>}                                 # Entity based on nouns
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens with the chunk parser
parsed_tree = chunk_parser.parse(tagged)

# Print the output
print(parsed_tree)
parsed_tree.draw()  # This will display the chunk tree visually if running in a suitable environment
