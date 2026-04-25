
{% p = CurrentPageInfo.NodeAliasPath.Split("/",true) #%}
{% 
    count = 0;
    foreach (x, index in enumerate(p)) {
      href = "";
      for(i = 0; i <= index; i++){
        href = href + p[i] + "/";
      }
      print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-"," ") + "&lt;/span&gt;&lt;/a&gt;"); 
      print("&lt;meta itemprop='position' content='" + (index + 1) + "' /&gt;");  // Adjusted to use index + 1
      print("&lt;/li&gt;");
    }
    #%} 
