
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%} 
{% 
    count = 0;
    foreach (x in p) {
      href = "";
      for (i = 0; i < count; i++) {
        href = href + p[i] + "/";
      }

      // Updated meta position logic
      position = count + 1; // Position starts at 1 for the home page

      print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
      print("<a itemprop='item' href='/" + href + "'>");
      print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
      print("</a>");
      print("<meta itemprop='position' content='" + position + "' />");
      print("</li>");

      count++;
    }
%}
