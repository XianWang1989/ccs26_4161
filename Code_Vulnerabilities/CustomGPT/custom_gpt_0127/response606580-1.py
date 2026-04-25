
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  # Start the position counter at 1
    foreach (x in p) {
      href = "";
      for(i = 0; i < count; i++){
        href = href + p[i] + "/";
      }
      print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
      print("<a itemprop='item' href='/" + href + "'>");
      print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
      print("</a>");
      print("<meta itemprop='position' content='" + count + "' />");  # Use count for position
      print("</li>");
      count++;  # Increment count for the next position
    }
    #%}
