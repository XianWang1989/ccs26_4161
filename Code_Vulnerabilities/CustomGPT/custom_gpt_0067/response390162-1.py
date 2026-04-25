
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the phrase
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the grammar for cascading chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media type (optional DT, adjectives, NNs)
  RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}            # Relation (verb followed by a media type)
  ENTITY: {<NN.*>}                               # Entity (nouns)
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunks = chunk_parser.parse(tagged_tokens)

# Displaying the chunks
print(chunks)
chunks.draw()  # This will display a tree structure if using an interactive environment
