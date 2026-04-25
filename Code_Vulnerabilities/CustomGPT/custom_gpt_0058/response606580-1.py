
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    stack = "";
    for (index in range(0, p.length)) {
      href = "";
      for (i = 0; i <= index; i++) {
        href = href + p[i] + "/";
      }
      position = index + 1;  // Set position (1-based index)
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + p[index].Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + position + "' /&gt;"); 
      print("&lt;/li&gt;");
    }
    #%} 
