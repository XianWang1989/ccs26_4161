
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0;  // Initialize count for position
    foreach (x in p) {
        href = "";
        for (i = 0; i <= count; i++) {
            href = href + p[i] + "/";
        }

        // Output breadcrumb item
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
        print("<a itemprop='item' href='/" + href + "'>");
        print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
        print("</a>");

        // Output position meta tag
        print("<meta itemprop='position' content='" + (count + 1) + "' />");

        print("</li>");
        count++;  // Increment count for the next item
    }
%} 
