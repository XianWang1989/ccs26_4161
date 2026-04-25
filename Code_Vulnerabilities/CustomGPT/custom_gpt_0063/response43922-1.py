
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Text</title>
</head>
<body>
    <p style="color: blue; font-size: 24px;">This text is blue and bigger!</p>
</body>
</html>
"""

with open("styled_text.html", "w") as file:
    file.write(html_code)
