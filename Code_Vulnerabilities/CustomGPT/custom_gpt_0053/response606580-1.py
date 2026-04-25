
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  // Start the count from 1
    foreach (x in p) {
      href = "";
      for(i = 0; i < count; i++){
        href = href + p[i] + "/";
      }
      // Output breadcrumb item
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
      print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      // Output position meta tag
      print("&lt;meta itemprop='position' content='" + count + "' /&gt;");
      print("&lt;/li&gt;");
      count++;  // Increment position for the next item
    }
%}
