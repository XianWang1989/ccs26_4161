
# Custom function to mark specific words before chunking
def mark_specific_words(tagged_tokens):
    modified_tokens = []
    for word, tag in tagged_tokens:
        if word in ["directed", "acted"]:
            modified_tokens.append((word, "V_SPEC"))  # Mark specific verbs
        else:
            modified_tokens.append((word, tag))
    return modified_tokens

# Apply the function
modified_tagged_tokens = mark_specific_words(tagged_tokens)
chunked_sentence = chunk_parser.parse(modified_tagged_tokens)
print(chunked_sentence)
