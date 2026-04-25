
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances directed by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                          # Media NPs
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+|<VB.*> "directed"|<VB.*> "acted"} # Relations
  ENTITY: {<NN.*>}                                    # Entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
result = chunk_parser.parse(tagged)

# Display the result
print(result)
result.draw()  # Visualization of the parse tree
