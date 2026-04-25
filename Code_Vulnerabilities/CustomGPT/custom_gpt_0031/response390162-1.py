
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Step 1: Tokenize and POS Tagging
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Step 2: Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media noun phrase
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}             # Relation with media
  ENTITY: {<NN.*>}                               # General entity
"""

# Step 3: Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Step 4: Chunk the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Step 5: Display the chunked tree
print(chunked)

# Optional: Visualize the chunks
chunked.draw()
