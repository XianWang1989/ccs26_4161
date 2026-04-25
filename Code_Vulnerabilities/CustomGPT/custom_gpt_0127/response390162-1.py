
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize and tag parts of speech
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Media NPs
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                # Relation verb followed by a noun phrase
    ENTITY: {<NNP>+}                                   # Named entity, e.g. proper nouns
"""

# Create a parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked result
print(chunked)

# To visualize the chunks using NLTK's tree visualization (install matplotlib if not available)
# chunked.draw()
