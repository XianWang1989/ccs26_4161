
# Create a function to check for indentation type
def check_indentation(code):
    lines = code.split('\n')
    for line in lines:
        if line.startswith(' '):
            print(f"Line '{line}' uses spaces")
        elif line.startswith('\t'):
            print(f"Line '{line}' uses tabs")

# Example code
code_snippet = '''
def getText(nodelist):
    """Description"""
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc
'''
check_indentation(code_snippet)
