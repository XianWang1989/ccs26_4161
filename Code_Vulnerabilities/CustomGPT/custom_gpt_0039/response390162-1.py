
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize the sentence and perform POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Noun phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}         # Verbs followed by noun phrases
  ENTITY: {<NN.*>}                           # Simple noun entities
"""

# Initialize the parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked_tree = chunk_parser.parse(tagged_tokens)

# Print the resulting chunked tree
print(chunked_tree)

# Optionally, to extract specific words for chunking
def extract_specific_words(tree, word_list):
    for subtree in tree.subtrees():
        if subtree.label() in ['MEDIA', 'RELATION', 'ENTITY']:
            for word in subtree.leaves():
                if word[0].lower() in word_list:
                    print(f"Found specific word: {word[0]} in {subtree.label()}")

# Checking for specific words like 'directed' or 'acted'
specific_words = ['directed', 'acted']
extract_specific_words(chunked_tree, specific_words)
