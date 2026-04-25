
def getText(nodelist):
    """Extracts the text between XML tags.

    I took this directly from http://docs.python.org/library/xml.dom.minidom.html.
    For example, if I have a tag <Tag>525</Tag>, this method returns me '525'.
    """
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data  # You can also use rc += node.data for conciseness
    return rc
