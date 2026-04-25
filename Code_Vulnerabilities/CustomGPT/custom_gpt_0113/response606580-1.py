
{% p = CurrentPageInfo.NodeAliasPath.Split("/", true) %}
{%
    count = 0;
    foreach (x in p) {
        href = "";
        for(i = 0; i <= count; i++) {
            href = href + p[i] + "/";
        }
        position = count + 1;  // Position starts at 1
        print("&lt;li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'&gt;");
        print("&lt;a itemprop='item' href='/" + href + "'&gt;&lt;span itemprop='name'&gt;" + x.Replace("-", " ") + "&lt;/span&gt;&lt;/a&gt;");
        print("&lt;meta itemprop='position' content='" + position + "' /&gt;");
        print("&lt;/li&gt;");
        count++;
    }
%}
