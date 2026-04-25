
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .styled-text {
            color: blue;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <p class="styled-text">This text is blue and larger!</p>
</body>
</html>
"""

# Save to an HTML file
with open("styled_text.html", "w") as file:
    file.write(html_content)
