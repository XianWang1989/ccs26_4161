
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%}
{% 
    count = 0; 
    foreach (x in p) {
        href = "";
        for (i = 0; i <= count; i++) {
            href = href + p[i] + "/";
        }
        // Print breadcrumb item
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
        print("<a itemprop='item' href='/" + href + "'>");
        print("<span itemprop='name'>" + x.Replace("-", " ") + "</span></a>");

        // Use 'count' as position (starts from 1 for breadcrumb)
        print("<meta itemprop='position' content='" + (count + 1) + "' />");

        print("</li>");
        count++;
    }
%}
