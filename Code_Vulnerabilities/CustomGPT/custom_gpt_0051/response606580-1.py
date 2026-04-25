
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0; // this will track the position
    foreach (x in p) {
      href = "";
      for(i = 0; i <= count; i++){
        href = href + p[i] + "/";
      }
      // Output the breadcrumb list item
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-"," ") + "&lt;/span&gt;&lt;/a&gt;"); 
      // Output the position using count + 1
      print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");
      print("&lt;/li&gt;");
      count++; // increment the counter
    }
    #%} 
