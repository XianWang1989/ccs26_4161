
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag parts of speech
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create the chunker
chunker = RegexpParser(grammar)

# Apply the chunker to the tagged tokens
chunked = chunker.parse(tagged)

# Display the results
print(chunked)
