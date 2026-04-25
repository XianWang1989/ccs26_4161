
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>} | {<NNP>}     # Include proper nouns
"""

# Create a chunk parser
chunker = RegexpParser(grammar)

# Apply the chunker to the tagged sentence
result = chunker.parse(tagged)

# Print the results
print(result)
result.draw()  # Visualize the chunking output
