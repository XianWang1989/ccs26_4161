
def chunk_text(text):
    # Tokenize and POS tag the text
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    # Initialize the chunk parser
    chunk_parser = RegexpParser(grammar)

    # Chunk the tagged text
    chunked = chunk_parser.parse(tagged)
    return chunked
