
{% 
    p = CurrentPageInfo.NodeAliasPath.Split("/", true);
    position = 1;  // Initialize a position counter

    foreach (x in p) {
      href = "";
      for(i = 0; i < position; i++){
        href = href + p[i] + "/";
      }

      print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
      print("<a itemprop='item' href='/" + href + "'>");
      print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
      print("</a>");
      print("<meta itemprop='position' content='" + position + "' />");  // Use position counter here
      print("</li>");

      position++;  // Increment position for the next item
    }
%}
