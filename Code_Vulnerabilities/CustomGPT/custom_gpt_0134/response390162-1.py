
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define your grammar rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                # Chunk sequences of DT, JJ, NN
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}       # Chunk verbs followed by NPs
  ENTITY: {<NN.*>}                          # Chunk singular/plural nouns
"""

# Create the parser
chunker = RegexpParser(grammar)

# Apply the chunking
chunked = chunker.parse(tagged)

# Visualizing the tree
print(chunked)

# Extracting specific words (e.g. "directed" or "acted") as part of the RELATION
for subtree in chunked.subtrees():
    if subtree.label() == 'RELATION':
        print("Relation found:", ' '.join(word for word, pos in subtree.leaves()))
