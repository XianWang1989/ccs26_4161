
import nltk
from nltk import RegexpParser, pos_tag, word_tokenize

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA:     {<DT>?<JJ>*<NN.*>+}                    # Media
  RELATION:  {<VB.*><DT>?<JJ>*<NN.*>+}              # Related verbs with noun phrases
  ENTITY:    {<NN.*>}                               # Entities
  PP:        {<IN><MEDIA>}                          # Preposition phrase followed by MEDIA
  VP:        {<VB.*><MEDIA|ENTITY|PP>+$}            # Verb phrase
  CLAUSE:    {<MEDIA><VP>}                          # Clause structure
"""

# Create a parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
parsed_tree = chunk_parser.parse(tagged)

# Display the result
print(parsed_tree)

# Optionally, to visualize the chunk tree
parsed_tree.draw()
