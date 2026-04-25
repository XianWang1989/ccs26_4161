
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 1;  # Start position at 1 for the first item
    foreach (x in p) {
      href = "";
      for (i = 0; i < p.Length; i++) {  # Use Length to avoid index issues
        if (i <= count - 1) {  # Ensure it only adds until current item
          href = href + p[i] + "/";
        }
      }
      print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
      print("<a itemprop='item' href='/" + href + "'><span itemprop='name'>" + x.Replace("-", " ") + "</span></a>");
      print("<meta itemprop='position' content='" + count + "' />");
      print("</li>");
      count++;  # Increment position for the next item
    }
}%}
