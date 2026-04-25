
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Media noun phrases
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                # Relations with verbs and noun phrases
    ENTITY: {<NN.*>}                                   # General entity
"""

# Create a chunk parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Display the chunking results
print(chunked)

# Draw the chunk tree for visualization (optional, requires a GUI backend)
chunked.draw()

# To specifically match certain verbs
for subtree in chunked.subtrees():
    if subtree.label() == 'RELATION':
        for word, pos in subtree.leaves():
            if word in ["directed", "acted"]:  # Specify your specific words here
                print(f'Matching Relation Found: {subtree}')
