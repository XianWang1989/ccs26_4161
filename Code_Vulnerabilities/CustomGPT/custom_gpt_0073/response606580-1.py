
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) #%}
{%
    count = 1;  // Start counting from 1 for the position
    foreach (x in p) {
        href = "";
        for (i = 0; i < p.Length; i++) {
            if (i <= count - 1) {
                href = href + p[i] + "/";
            }
        }
        print("<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'>");
        print("<a itemprop='item' href='/" + href + "'>");
        print("<span itemprop='name'>" + x.Replace("-", " ") + "</span>");
        print("</a>");
        print("<meta itemprop='position' content='" + count + "' />");
        print("</li>");
        count++;
    }
%}
