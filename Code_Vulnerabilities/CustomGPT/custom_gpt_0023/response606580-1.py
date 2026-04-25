
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  // Start position from 1
    foreach (x in p) {
        href = "";

        // Build the path for the current breadcrumb
        for (i = 0; i < count; i++) {
            href += p[i] + "/";
        }

        // Output breadcrumb item
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
        print("<a itemprop='item' href='/" + href + "'>");
        print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
        print("</a>");

        // Output position
        print("<meta itemprop='position' content='" + count + "' />");
        print("</li>");

        count++;  // Increment position for the next item
    }
%}
