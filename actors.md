---
title: Aktorzy
---
<nav>
    {% for item in site.data.navigation %}
      <a href="{{ item.link }}" {% if page.url == item.link %}style="color: red;"{% endif %}>
        {{ item.name }}
      </a>
    {% endfor %}
  </nav>
<h1>Lista aktorów</h1>

<ul>
  {% for actor in site.actors %}
    <li>
      <h2><a href="{{ actor.url }}">{{ actor.name }}</a></h2>
      <img src = "{{ actor.image }}">
      <p>
      <br>
      </p>
    </li>
  {% endfor %}
</ul>