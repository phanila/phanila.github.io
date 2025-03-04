---
layout: default
title: O mnie
---
<nav>
  {% for item in site.data.navigation %}
    <a href="{{ item.link }}" {% if page.url == item.link %}style="color: red;"{% endif %}>
      {{ item.name }}
    </a>
  {% endfor %}
</nav>

# O mnie

Ta strona mówi o mnie, czego jak widać nie ma dużo.