
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB(?:.*|directed|acted)><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Example sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag
tokenized_sentence = word_tokenize(sentence)
tagged_sentence = pos_tag(tokenized_sentence)

# Create chunker
chunker = RegexpParser(grammar)

# Chunk the sentence
chunked_sentence = chunker.parse(tagged_sentence)

# Display the chunked sentence
print(chunked_sentence)
chunked_sentence.draw()  # Open tree visualization
