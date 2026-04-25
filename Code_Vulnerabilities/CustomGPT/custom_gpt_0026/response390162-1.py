
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Media: Optional DT, any JJ, followed by one or more NNs
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}        # Relation: Verb followed by optional DT, any JJ, followed by one or more NNs
  ENTITY: {<NN.*>}                           # Entity: Just a noun
"""
