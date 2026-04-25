
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    counter = 1;  // Start counting from 1 for the position
    foreach (x in p) {
      href = "";
      for(i = 0; i < counter; i++){
        href = href + p[i] + "/";
      }
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + counter + "' /&gt;");  // Use the counter for position
      print("&lt;/li&gt;");
      counter++;  // Increment counter for the next item
    }
    #%}
