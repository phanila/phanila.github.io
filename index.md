---
title: Home
---
<nav>
  {% for item in site.data.navigation %}
    <a href="{{ item.link }}" {% if page.url == item.link %}style="color: red;"{% endif %}>
      {{ item.name }}
    </a>
  {% endfor %}
</nav>

# Lista najlepszych aktorów

Mój stary to prawdziwy fanatyk filmów. Zna się na wszystkim – od klasyków po nowości. Kazał nam obejrzeć Ben-Hura, a w trakcie filmu zaczyna: „A ten aktor? Skąd go znasz?”. Potem podaje pierwszą podpowiedź: „Pamiętasz, gdzie grał?”. Wiadomo, że jak nie zgadniesz, to będzie kolejna: „A ten? Podpowiedź: grał w filmie nawiązującym do Casablanki”.

Zawsze rzuca kolejne trudniejsze zagadki, w stylu: „W tym filmie był złym gościem, ale potem zmienił stronę”. Tak mija cały wieczór – zgadujesz, ale i tak zawsze zapominasz, gdzie ostatnio widziałeś tych aktorów.

Po to właśnie powstała ta strona, bym mogła sobie utrwalić nazwiska aktorów.

[link do listy aktorów](/actors.html)