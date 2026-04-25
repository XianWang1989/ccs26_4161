
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the phrase
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                          # Chunk sequences of DT, JJ, NN for media
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                 # Chunk verbs followed by media
  ENTITY: {<NN.*>}                                    # Chunk any single noun
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged_tokens)

# Display the result
print(chunked)
chunked.draw()  # This will visualize the chunked structure
