
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  # Start counting from 1 for the first item
    foreach (x in p) {
        href = "";
        for(i = 0; i < count; i++){
            href = href + p[i] + "/";
        }
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
        print("<a itemprop='item' href='/" + href + "'>");
        print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
        print("</a>");
        print("<meta itemprop='position' content='" + count + "' />");  # Use count directly for position
        print("</li>");
        count++;  # Increment the counter for each breadcrumb item
    }
%}
