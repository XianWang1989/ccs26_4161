
# Make sure the following lines are indented with spaces only
def getText(nodelist):
    """Docstring here."""
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data
    return rc
