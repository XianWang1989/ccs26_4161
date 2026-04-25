
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}              # Media noun phrases
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}     # Relation phrases
  ENTITY: {<NN.*>}                        # Entities
"""

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokenized_sentence = word_tokenize(sentence)
tagged_sentence = pos_tag(tokenized_sentence)

# Parse the sentence using the chunk parser
chunked_sentence = chunk_parser.parse(tagged_sentence)

# Display the chunked output
print(chunked_sentence)

# To visualize the chunks, you can use this:
chunked_sentence.draw()
