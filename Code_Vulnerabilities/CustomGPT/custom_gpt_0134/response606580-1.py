
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%}
{% 
    count = 0;  // Counter for position
    foreach (x in p) {
      href = "";
      for(i = 0; i <= count; i++){
        href = href + p[i] + "/";
      }
      // Print the breadcrumb item
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      // Print the position meta
      print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;"); // Use count + 1 for position
      print("&lt;/li&gt;");
      count++;
    }
    #%}
