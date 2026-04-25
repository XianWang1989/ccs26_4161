
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Step 1: Tokenize the text
tokens = word_tokenize(text)

# Step 2: Perform POS tagging
tagged_tokens = pos_tag(tokens)

# Step 3: Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                      # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}              # Chunk verb followed by media
  ENTITY: {<NN.*>}                                # Chunk single nouns
"""

# Step 4: Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Step 5: Parse the input and extract chunks
parsed_chunks = chunk_parser.parse(tagged_tokens)

# Printing the result
print(parsed_chunks)

# To visualize nicely
parsed_chunks.draw()
