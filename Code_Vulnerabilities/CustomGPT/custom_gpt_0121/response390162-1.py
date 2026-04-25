
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing the sentence
tokens = word_tokenize(sentence)
# Part-of-speech tagging
tagged_tokens = pos_tag(tokens)

# Define the grammar with multiple rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}  # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}  # Verbs followed by a noun phrase
  ENTITY: {<NN.*>}  # Noun entities
  """

# Create a RegexpParser with the defined grammar
chunker = RegexpParser(grammar)

# Perform chunking
chunked = chunker.parse(tagged_tokens)

# Display the result
print(chunked)

# Draw the chunk tree for visualization (optional)
# chunked.draw()

# Extract specific words (e.g., 'directed', 'acted') within RELATION
for subtree in chunked.subtrees():
    if subtree.label() == 'RELATION':
        for word, tag in subtree.leaves():
            if word in ['directed', 'acted']:
                print(f"Relation found: {subtree}")
