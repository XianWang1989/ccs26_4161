
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by sam mendes"

# Tokenize and POS tag the text
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Media
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                # Relation
  ENTITY: {<NN.*>}                                   # Entity
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Chunk the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked result
print(chunked)

# Visualize the chunked structure
chunked.draw()
