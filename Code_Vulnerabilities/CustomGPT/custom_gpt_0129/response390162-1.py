
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Define a cascading grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                           # Chunk sequences of DT, JJ, NN
    RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}}                # Chunk verbs followed by MEDIA
    ENTITY: {<NN.*>}                                     # Chunk single nouns
"""

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Display the chunked structure
print(chunked)

# Now to extract specific words like "directed" or "acted"
# You can apply a filter to search for specific relations
for subtree in chunked.subtrees():
    if subtree.label() == 'RELATION':
        for word, tag in subtree.leaves():
            if word.lower() in ['directed', 'acted']:
                print(f"Found relation: {word}")
