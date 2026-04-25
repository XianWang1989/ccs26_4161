
import nltk
from nltk import RegexpParser, pos_tag
from nltk.tokenize import word_tokenize

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by a famous director"

# Tokenize and POS tag the phrase
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunks = chunk_parser.parse(tagged_tokens)

# Print the results
print(chunks)

# Visualize the chunk tree
chunks.draw()
