
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Ensure you have the necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                      # Chunk sequences of DT, JJ, NN
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}            # Chunk verbs followed by NP
    ENTITY: {<NN.*>}                               # Chunk entities
"""

# Create a parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Example phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenization and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Perform chunking
chunks = chunk_parser.parse(tagged)

# Output the chunks
print("Chunks:")
print(chunks)

# Visualizing the chunk tree (optional)
chunks.draw()
