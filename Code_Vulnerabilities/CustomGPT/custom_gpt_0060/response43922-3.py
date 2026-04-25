
# Example HTML with inline CSS to change color and size
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .blue-text {
            color: blue;
            font-size: 24px; /* Larger font size */
        }
    </style>
</head>
<body>
    <p class="blue-text">This text is blue and bigger!</p>
</body>
</html>
"""

# Save to an HTML file
with open("example.html", "w") as file:
    file.write(html_content)
