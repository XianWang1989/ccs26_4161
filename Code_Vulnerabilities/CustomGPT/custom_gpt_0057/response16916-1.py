
def getText(nodelist):
    """Extracts the text between XML tags

    I took this directly from http://docs.python.org/library/xml.dom.minidom.html.
    For example, if I have a tag <Tag>525</Tag> this method returns me '525'
    """
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

def test_getText():
    class MockNode:
        TEXT_NODE = 3

        def __init__(self, data):
            self.nodeType = self.TEXT_NODE
            self.data = data

    nodelist = [MockNode("525")]
    assert getText(nodelist) == "525", "Test failed!"
    print("Test passed!")

test_getText()
