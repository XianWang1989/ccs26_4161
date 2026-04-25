
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    position = 1;  // Start with the first position
    foreach (x in p) {
      href = "";
      for(i = 0; i < position; i++){
        href = href + p[i] + "/";
      }
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + position + "' /&gt;");  // Use the position counter here
      print("&lt;/li&gt;");
      position++;  // Increment the position for the next item
    }
    #%} 
