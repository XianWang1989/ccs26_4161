
{% p = CurrentPageInfo.NodeAliasPath.Split("/",true) #%} 
{% 
    counter = 1;  // Start counting positions from 1
    foreach (x in p) {
      href = "";
      for(i = 0; i < counter; i++){
        href = href + p[i] + "/";
      }
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
      print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-"," ") + "&lt;/span&gt;&lt;/a&gt;");
      print("&lt;meta itemprop='position' content='" + counter + "' /&gt;");
      print("&lt;/li&gt;");
      counter++;  // Increment the counter after each loop
    }
{% } %}
