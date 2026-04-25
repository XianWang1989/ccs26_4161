
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0;
    position = 1;  // Initialize the position counter
    foreach (x in p) {
        href = "";
        for(i = 0; i <= count; i++) {
            href = href + p[i] + "/";
        }
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
        print("&lt;meta itemprop='position' content='" + position + "' /&gt;"); // Use the position variable
        print("&lt;/li&gt;");
        count++;
        position++; // Increment the position counter
    }
%}
