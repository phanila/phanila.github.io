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
<label for="file">Procent aktorów pokazanych na tej stronie</label>
<progress id="file" value="32" max="100"> 1% </progress>
<h1>Lista aktorów</h1>
<a href="https://www.filmweb.pl/ranking/person/actors/male">Źródło</a>

<ol>
{% for actor in site.actors %}
    <li>
      <h2><a href="{{ actor.url }}">{{ actor.name }}</a></h2>
      {{ "![Photo](" | append: actor.image | append: ")" | markdownify }}
    </li>
{% endfor %}
</ol>