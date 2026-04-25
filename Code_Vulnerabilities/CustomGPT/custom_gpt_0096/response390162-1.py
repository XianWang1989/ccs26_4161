
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "Adventure movies between 2000 and 2015 featuring performances by Daniel Craig."

# Tokenize and POS tag
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Define your cascading chunk grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}  # Media
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}  # Relation with verbs
  ENTITY: {<NNP>+}  # Named entities
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
parsed_tree = chunk_parser.parse(tagged_tokens)

# Print the result
print(parsed_tree)
parsed_tree.draw()  # Visual representation if you have a GUI environment
