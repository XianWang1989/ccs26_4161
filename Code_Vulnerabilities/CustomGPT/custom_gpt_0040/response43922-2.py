
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .blue-text {
            color: blue;
            font-size: 24px; /* Make text bigger */
        }
    </style>
</head>
<body>
    <p class="blue-text">This text is blue and bigger!</p>
</body>
</html>
"""

# Output to an HTML file
with open("output.html", "w") as file:
    file.write(html_content)

print("HTML file created with styled text.")
