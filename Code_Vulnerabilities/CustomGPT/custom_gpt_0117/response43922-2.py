
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        .blue-text {
            color: blue;
            font-size: 20px; /* Adjust size as needed */
        }
    </style>
</head>
<body>
    <p class="blue-text">This text is blue and bigger!</p>
</body>
</html>
'''

# Write to an HTML file
with open("output.html", "w") as f:
    f.write(html_content)

print("HTML file created: output.html")
