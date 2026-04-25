
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0;  // Keep track of the index for position
    foreach (x in p) {
        href = "";
        for (i = 0; i <= count; i++) {
            href = href + p[i] + "/";
        }

        // Position is count + 1 because positions start from 1
        position = count + 1;

        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
        print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
        print("&lt;meta itemprop='position' content='" + position + "' /&gt;");
        print("&lt;/li&gt;");

        count++;
    }
%}
