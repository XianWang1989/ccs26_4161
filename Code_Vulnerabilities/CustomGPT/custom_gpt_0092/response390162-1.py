
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Step 1: Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Step 2: Create a sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Step 3: Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Step 4: Create a chunk parser using the defined grammar
chunk_parser = RegexpParser(grammar)

# Step 5: Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Step 6: Display the chunked result
print(chunked)

# Optional: Draw the chunk tree
chunked.draw()
