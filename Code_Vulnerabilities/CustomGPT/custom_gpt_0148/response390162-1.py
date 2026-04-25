
import nltk
from nltk import pos_tag, ne_chunk
from nltk.chunk import RegexpParser

# Sample phrase to analyze
phrase = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig directed by Sam Mendes."

# Tokenize and POS tag the sentence
tokens = nltk.word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}  # Specifying specific relation verbs can be done using separate rules
  ENTITY: {<NN.*>}  # Entities can just be noun phrases
  """
# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Display the chunked output
print(chunked)

# For visual representation, you can also use
chunked.draw()
