
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "Adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize and POS Tagging
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                        # Chunk for media
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}               # Relation chunk with verb followed by NPs
  ENTITY: {<NNP+>}                                   # Proper nouns as entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the POS tagged words
chunked = chunk_parser.parse(pos_tags)

# Print the chunked structure
print(chunked)

# Visualize the chunking (Optional, requires matplotlib and nltk library)
# chunked.draw()
