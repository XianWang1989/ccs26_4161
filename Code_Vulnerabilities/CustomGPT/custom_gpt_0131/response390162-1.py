
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by a famous director"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar with cascaded chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Chunk for media
  RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}}               # Chunk for relations
  ENTITY: {<NN.*>}                                   # Chunk for named entities
  ACTION: {<VBD|VBN|VBP> <DT>?<JJ>*<NN.*>+}          # Chunk for actions (for specific verbs)
"""

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Perform the chunking
chunks = chunk_parser.parse(tagged)

# Display the results
print(chunks)
chunks.draw()  # Optional: This will visually display the chunk structure
