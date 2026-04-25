
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig directed by Sam Mendes"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}}
    ENTITY: {<NN.*>}
    PP: {<IN><NP>}
    VP: {<VB.*><NP|PP>*}  # Including PP as arguments
    CLAUSE: {<NP><VP>}    # Chunk NP, VP
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged)

# Print the results
print(chunked)

# Visualize chunk tree (optional)
chunked.draw()
