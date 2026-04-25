
{% p = CurrentPageInfo.NodeAliasPath.Split("/",true) #%} 
{% 
    # Initialize the counter
    count = 1;  # Start counting from 1 since schema.org uses 1-based indexing
    foreach (x in p) {
      href = "";
      for(i = 0; i < count; i++){
        href = href + p[i] + "/";
      }

      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-"," ") + "&lt;/span&gt;&lt;/a&gt;");

      # Use the current count for the meta:position
      print("&lt;meta itemprop='position' content='" + count + "' /&gt;");
      print("&lt;/li&gt;");

      count++;  # Increment the counter for the next item
    }
%} 
