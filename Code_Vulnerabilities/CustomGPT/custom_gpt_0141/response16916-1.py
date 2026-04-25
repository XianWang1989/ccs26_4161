
def getText(nodelist):
    """Extracts the text between XML tags

    I took this directly from http://docs.python.org/library/xml.dom.minidom.html.
    For example, if I have a tag <Tag>525</Tag> this method returns me '525'
    """
    rc = ""  # Initialize an empty string to hold the result
    for node in nodelist:  # Iterate through each node in nodelist
        if node.nodeType == node.TEXT_NODE:  # Check if the node is a text node
            rc = rc + node.data  # Concatenate the node data to rc
    return rc  # Return the concatenated result
