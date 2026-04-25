
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%}
{% 
    count = 0;
    foreach (x in p) {
      href = "";
      for(i = 0; i <= count; i++){
        href = href + p[i] + "/";
      }
      position = count + 1;  // Adjusting position for 1-based indexing
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
      print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + position + "' /&gt;");  // Use the position variable here
      print("&lt;/li&gt;");
      count++;
    }
    #%} 
