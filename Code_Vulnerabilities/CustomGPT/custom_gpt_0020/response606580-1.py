
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  // Start position from 1
    foreach (x in p) {
      href = "";
      for(i = 0; i < count; i++){
        href = href + p[i] + "/";
      }
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + count + "' /&gt;");  // Use `count` directly here
      print("&lt;/li&gt;");
      count++;  // Increment the count for next item
    }
    #%} 
