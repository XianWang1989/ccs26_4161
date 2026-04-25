
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  // Start counter from 1 for positions
    foreach (x in p) {
      href = "";
      for(i = 0; i < count; i++){
        href = href + p[i] + "/";
      }
      print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
      print("<a itemprop='item' href='/" + href + "'>");
      print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
      print("</a>");

      // Set meta position using the count variable
      print("<meta itemprop='position' content='" + count + "' />");
      print("</li>");

      count++;  // Increment position for next item
    }
    #%}
