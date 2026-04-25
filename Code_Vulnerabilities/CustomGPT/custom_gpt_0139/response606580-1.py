
{% 
    p = CurrentPageInfo.NodeAliasPath.Split("/", true);
    count = 0;  // Initialize counter for position
    foreach (x in p) {
        href = "";
        for (i = 0; i <= count; i++) {
            href = href + p[i] + "/";
        }

        // Output the breadcrumb list item with title and link
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
        print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;");

        // Output the position for the breadcrumb item
        print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");  // Populate position as count + 1
        print("&lt;/li&gt;");

        count++;  // Increment the position counter
    }
%}
