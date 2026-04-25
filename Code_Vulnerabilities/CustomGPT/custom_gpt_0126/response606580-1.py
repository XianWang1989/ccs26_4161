
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    for count, x in enumerate(p) {
      href = "";
      for i in range(count + 1) {
        href += p[i] + "/";
      }
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");  // Increment position by 1
      print("&lt;/li&gt;");
    }
    #%}
