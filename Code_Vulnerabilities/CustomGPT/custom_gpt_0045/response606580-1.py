
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0; 
    foreach (x in p) { 
        href = ""; 
        // Build href by traversing through the array 
        for (i = 0; i <= count; i++) { 
            href = href + p[i] + "/"; 
        } 
        // Output the list item for breadcrumb 
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;"); 
        print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
        // Set the position using count + 1 to start from 1 
        print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;"); 
        print("&lt;/li&gt;"); 
        count++; 
    } 
%}
