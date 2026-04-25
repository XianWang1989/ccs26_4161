
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%}
{% 
    print("<ul itemscope itemtype='http://schema.org/BreadcrumbList'>")
    for count, x in enumerate(p):
        href = "/".join(p[:count + 1]) + "/"
        position = count + 1  # Positions are 1-based
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>")
        print("<a itemprop='item' href='/" + href + "'>")
        print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>")
        print("</a>")
        print("<meta itemprop='position' content='" + str(position) + "' />")
        print("</li>")
    print("</ul>")
%}
