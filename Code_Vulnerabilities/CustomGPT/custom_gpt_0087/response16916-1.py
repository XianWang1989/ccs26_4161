
def getText(nodelist):
    """Extracts the text between XML tags

    This comments follows consistent indentation.
    For example, if I have a tag <Tag>525</Tag>, this method returns '525'.
    """
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc
