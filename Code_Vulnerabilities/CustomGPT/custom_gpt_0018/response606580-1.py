
# Assuming p is the list of page paths, split from CurrentPageInfo.NodeAliasPath
p = CurrentPageInfo.NodeAliasPath.split("/", True)

# Start generating the breadcrumb HTML
html_output = ""

for count, x in enumerate(p):
    href = "/".join(p[:count + 1]) + "/"
    position = count + 1  # Set position as count + 1 (1-based index)

    html_output += f"<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>"
    html_output += f"<a itemprop='item' href='/{href}'><span itemprop='name'>{x.replace('-', ' ')}</span></a>"
    html_output += f"<meta itemprop='position' content='{position}' />"
    html_output += "</li>"

# Print or return the generated HTML output
print(html_output)
