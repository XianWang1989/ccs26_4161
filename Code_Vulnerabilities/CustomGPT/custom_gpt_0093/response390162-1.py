
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}            # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}    # Chunk verbs followed by DT, JJ, NN
  ENTITY: {<NN.*>}                       # Chunk nouns
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunks = chunk_parser.parse(tagged)

# Display the chunks
print(chunks)

# Visualize chunking
chunks.draw()
