
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar with cascading chunks
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}              # Relation
    ENTITY: {<NN.*>}                                # Entity
    """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentences
chunked = chunk_parser.parse(tagged)

# Display the chunked tree
print(chunked)

# Optionally, you can iterate through the chunks
for subtree in chunked.subtrees():
    if subtree.label() in ['MEDIA', 'RELATION', 'ENTITY']:
        print(f"{subtree.label()}: {' '.join(word for word, tag in subtree.leaves())}")
