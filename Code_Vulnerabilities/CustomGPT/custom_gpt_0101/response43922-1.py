
# Example code to change text color and size in HTML using Python

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .blue {
            color: blue;
            font-size: 24px; /* Change to desired size */
        }
    </style>
</head>
<body>
    <p class="blue">This text is blue and larger!</p>
</body>
</html>
"""

# Save to an HTML file
with open("output.html", "w") as file:
    file.write(html_content)

# To run this, open output.html in a web browser
