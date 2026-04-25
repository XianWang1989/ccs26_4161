
def getText(nodelist):
    """Extracts the text between XML tags.

    This method returns the text content of the provided XML node list.
    For example, if I have a tag <Tag>525</Tag>, this method returns '525'.
    """
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data
    return rc
