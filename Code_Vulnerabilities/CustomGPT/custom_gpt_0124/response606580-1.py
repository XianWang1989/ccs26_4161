
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%}
{% 
    count = 0;
    foreach (x in p) {
      href = "";
      for(i = 0; i <= count; i++) {
        href = href + p[i] + "/";
      }

      // Print the breadcrumb list item
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
      print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;"); 

      // Print the position using count + 1 (since index starts from 0)
      print("&lt;meta itemprop='position' content='" + (count + 1) + "' /&gt;");

      print("&lt;/li&gt;");
      count++;
    }
%}
