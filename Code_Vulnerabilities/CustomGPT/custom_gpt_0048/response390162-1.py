
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunks = chunk_parser.parse(tagged)

# Display the chunks
print(chunks)
# Optional: visualize the chunks
chunks.draw()
