
{% p = CurrentPageInfo.NodeAliasPath.Split("/",true) #%} 
{% 
    count = 1;  // Start the counter at 1 for position
    for (i = 0; i < p.Length; i++) {
        href = "";
        for(j = 0; j <= i; j++){
            href = href + p[j] + "/";
        }
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + p[i].Replace("-"," ") + "&lt;/span&gt;&lt;/a&gt;"); 
        print("&lt;meta itemprop='position' content='" + count + "' /&gt;");
        print("&lt;/li&gt;");
        count++;  // Increment the position counter
    }
    #%} 
