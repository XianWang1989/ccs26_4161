
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}               # Chunk for Media
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}      # Chunk for Relations
  ENTITY: {<NN.*>}                         # Chunk for Entities
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged)

# Print the chunked structure
print(chunked)

# Visualize the chunking (optional, requires matplotlib)
try:
    import matplotlib.pyplot as plt
    from nltk.draw.tree import TreeView

    # Draw tree visualization
    tree = TreeView(chunked)
    plt.figure(figsize=(15, 10))
    tree.draw()
except ImportError:
    print("Matplotlib not available for visualization.")
