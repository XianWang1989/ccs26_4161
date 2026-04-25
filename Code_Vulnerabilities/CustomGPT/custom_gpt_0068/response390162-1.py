
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by some director"

# Step 1: Tokenize and Part-of-Speech Tagging
tokenized_sent = word_tokenize(text)
tagged_sent = pos_tag(tokenized_sent)

# Step 2: Define the grammar with cascading structures
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                  # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}        # Chunk verbs and their arguments
  ENTITY: {<NN.*>}                            # Chunk noun phrases
"""

# Step 3: Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Step 4: Parse the tagged sentence to create chunks
chunked_sent = chunk_parser.parse(tagged_sent)

# Step 5: Display the chunked output
print(chunked_sent)

# Step 6: Visualize the chunked tree (Optional)
chunked_sent.draw()
