
def getText(nodelist):
    """Extracts the text between XML tags.

    I took this directly from the Python documentation.
    For example, if I have a tag <Tag>525</Tag>, this method returns '525'.
    """
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data
    return rc
