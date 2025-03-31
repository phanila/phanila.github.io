---
title: Aktorzy
---
<label for="file">Procent aktorów pokazanych na tej stronie</label>
<progress id="file" value="32" max="100"> 1% </progress>
<h1>Lista aktorów</h1>
<a href="https://www.filmweb.pl/ranking/person/actors/male">Źródło</a>

<ol class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4 mt-5">
  {% for actor in site.actors %}
    <li class="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-300">
  <a href="{{ actor.url }}" class="block">
    <div class="grid items-center justify-center">
      <!-- Photo at the top -->
      <div class="w-32 h-32 mb-4 mx-auto">
        <img src="{{ actor.image }}" alt="{{ actor.name }}" class="w-full h-full object-cover rounded-lg">
      </div>
      <!-- Number below the photo -->
      <span class="flex-shrink-0 mx-auto w-8 h-8 bg-gray-200 rounded-lg text-center flex items-center justify-center mb-2">
        {{ actor.number }}
      </span>
      <!-- Name below the number -->
      <h2 class="text-center text-blue-900">
        {{ actor.name }}
      </h2>
    </div>
  </a>
</li>
  {% endfor %}
</ol>
