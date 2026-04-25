
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample input phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar with multiple rules
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}               # Media chunk
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}      # Relation chunk
    ENTITY: {<NN.*>}                         # Entity chunk
"""

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked output
print(chunked)

# To display specific words, you can further filter
for subtree in chunked.subtrees():
    if subtree.label() == 'RELATION':
        for word, tag in subtree.leaves():
            if word.lower() in ['directed', 'acted']:
                print(f"Specific word found in RELATION: {word}")
