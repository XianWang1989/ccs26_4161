
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  // Start count at 1 since list positions are usually 1-indexed
    foreach (x in p) {
        // Initialize href for the breadcrumb link
        href = "";

        // Build href for the current breadcrumb element
        for (i = 0; i < count; i++) {
            href = href + p[i] + "/";
        }

        // Print breadcrumb item
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
        print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
        print("&lt;meta itemprop='position' content='" + count + "' /&gt;"); // Use count for position
        print("&lt;/li&gt;");

        // Increment count for the next position
        count++;
    }
%}
