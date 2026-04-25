
import nltk
from nltk import TokenizerI
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by a great director"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                                 # Media noun phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                        # Relations
  ENTITY: {<NN.*>}                                          # Entities
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser to the tagged tokens
chunks = chunk_parser.parse(tagged)

# Display the chunks
print(chunks)

# Function to define specific words for chunking
def specific_verbs(verb_list):
    s_verbs = '|'.join(verb_list)
    return rf"""RELATION: {{<VB.*><DT>?<JJ>*<NN.*>+}}|{{<VB.?>{{({s_verbs})}}}}"""

# Incorporate specific verbs
specific_grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Define specific verbs
specific_verbs_list = ["directed", "acted"]
specific_grammar += f"\n{specific_verbs(specific_verbs_list)}"

# Create the chunk parser again with specific verbs
specific_chunk_parser = RegexpParser(specific_grammar)

# Apply the chunk parser to the tagged tokens
specific_chunks = specific_chunk_parser.parse(tagged)

# Display the specific chunks
print(specific_chunks)
