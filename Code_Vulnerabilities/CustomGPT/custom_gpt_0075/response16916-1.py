
def getText(nodelist):
    """Extracts the text between XML tags."""
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data
    return rc
