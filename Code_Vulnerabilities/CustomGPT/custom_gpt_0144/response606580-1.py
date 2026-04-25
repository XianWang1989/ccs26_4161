{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) %}
{% 
    count = 0
    total_breadcrumbs = p.Count  # Get the total number of breadcrumbs
    foreach (x in p) {
        href = ""
        for(i = 0; i <= count; i++){
            href = href + p[i] + "/"
        }
        position = count + 1  # Position starts at 1 for the Home page, etc.
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>")
        print("<a itemprop='item' href='/" + href + "'><span itemprop='name'>" + x.Replace("-", " ") + "</span></a>")
        print("<meta itemprop='position' content='" + position + "' />")
        print("</li>")
        count++
    }
 %}
