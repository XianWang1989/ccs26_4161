
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for cascading chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>} 
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
result = chunk_parser.parse(tagged)

# Print the parsed result
print(result)
result.draw()  # Visualize the chunked structure (optional)
