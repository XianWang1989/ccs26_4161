
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Define the sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}        # Chunk verbs followed by NP
  ENTITY: {<NN.*>}                          # Chunk single Nouns
  PP: {<IN><MEDIA>}                         # Chunk prepositions followed by MEDIA
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser to the tagged sentence
chunks = chunk_parser.parse(tagged)

# Print the resulting chunks
print(chunks)

# Optionally, visualize the chunks
chunks.draw()
