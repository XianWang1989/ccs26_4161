
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}             # Media noun phrase
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}    # Relation expression
  ENTITY: {<NN.*>}                        # Entity mention
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked result
print(chunked)

# Optionally draw the hierarchical structure
# chunked.draw()
