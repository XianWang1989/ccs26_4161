
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  // Start at 1 for the position
    foreach (x in p) {
      href = "";
      for(i = 0; i < count; i++) {
        href += p[i] + "/";
      }
      // Remove trailing slash for proper URL
      href = href.TrimEnd('/');

      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
      print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + count + "' /&gt;");
      print("&lt;/li&gt;");
      count++;  // Increment counter for next position
    }
    #%}
