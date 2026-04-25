
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0;  // Initialize position counter
    foreach (x in p) {
        href = "";
        for(i = 0; i <= count; i++){
            href = href + p[i] + "/";
        }
        // Create ListItem for breadcrumb
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
        print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;");

        // Use count + 1 for the position (since counting starts at 0)
        print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");

        print("&lt;/li&gt;");
        count++;  // Increment position counter
    }
%}
