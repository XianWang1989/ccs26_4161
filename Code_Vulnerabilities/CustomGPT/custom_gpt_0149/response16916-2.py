
class MockNode:
    TEXT_NODE = 3
    def __init__(self, data):
        self.nodeType = self.TEXT_NODE
        self.data = data

# Test
nodelist = [MockNode("525"), MockNode(" other text")]
print(getText(nodelist))  # Outputs: "525 other text"
