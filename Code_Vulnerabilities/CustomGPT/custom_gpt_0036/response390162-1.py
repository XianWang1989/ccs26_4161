
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenization and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Media noun phrase
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}         # Relation to entities
    ENTITY: {<NN.*>}                            # Entity noun
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform the chunking
result = chunk_parser.parse(tagged_tokens)

# Print the result
print(result)

# Drawing the chunk tree for visualization (optional)
result.draw()
