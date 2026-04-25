
html_content = '''
<p style="color:blue; font-size:20px;">This text is blue and bigger!</p>
'''

# To display it in a web application or save it to an HTML file
with open('output.html', 'w') as file:
    file.write(html_content)
