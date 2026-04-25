
def getText(nodelist):
    """Extracts the text between XML tags.

    This method returns the text content of XML elements, concatenated together.
    """
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data  # Concatenates text data
    return rc
