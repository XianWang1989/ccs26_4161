
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .blue-text {
            color: blue;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <p class="blue-text">This is blue and bigger text!</p>
</body>
</html>
"""

with open("styled_text.html", "w") as file:
    file.write(html_content)
