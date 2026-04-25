
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                            # Media nouns
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                   # Relations
  ENTITY: {<NN.*>}                                      # Entities
  """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Perform the chunking
chunked = chunk_parser.parse(tagged_words)

# Display the chunked tree
print(chunked)

# Optionally, to visualize the tree structure
chunked.draw()
