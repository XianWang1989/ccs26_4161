
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0;
    // This will hold the position for each breadcrumb item
    foreach (x in p) {
      href = "";
      for(i = 0; i <= count; i++) {
        href = href + p[i] + "/";
      }
      // Output the breadcrumb list item with schema markup
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 
      // Use count + 1 for the meta position (since count starts from 0)
      print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");
      print("&lt;/li&gt;");
      count++; // Increment the count for the next iteration
    }
%} 
