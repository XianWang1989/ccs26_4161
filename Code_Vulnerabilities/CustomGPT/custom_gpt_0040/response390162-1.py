
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for cascading chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                  # Media entities
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}         # Relations with NP following
  ENTITY: {<NN.*>}                            # Any noun
  PP: {<IN><MEDIA|ENTITY>}                    # Prepositions followed by MEDIA or ENTITY
  VP: {<VB.*><MEDIA|ENTITY|PP>+$}             # Verb phrases with associated MEDIA, ENTITY or PP
  CLAUSE: {<MEDIA|ENTITY><VP>}                # A clause of MEDIA or ENTITY followed by VP
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
parsed_tree = chunk_parser.parse(tagged_tokens)

# Display the parsed tree
print(parsed_tree)
parsed_tree.draw()  # Optional: to visualize the chunks
