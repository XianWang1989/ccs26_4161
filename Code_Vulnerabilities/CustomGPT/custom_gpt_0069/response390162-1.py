
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by sam mendes"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar for nested chunks
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
  """

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Display the chunked structure
print(chunked)

# Optional: To visualize the chunked tree
chunked.draw()
