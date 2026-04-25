
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{%
    count = 0;  # Initialize a counter for position
    foreach (x in p) {
      href = "";
      for(i = 0; i <= count; i++){
        href = href + p[i] + "/";
      }
      # Output the breadcrumb item
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;")
      print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 

      # Use count + 1 for position since positions start from 1
      print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");
      print("&lt;/li&gt;");
      count++;  # Increment the counter
    }
%} 
