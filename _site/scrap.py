from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from duckduckgo_search import DDGS
import time


# options = webdriver.ChromeOptions()
# options.binary_location = '/usr/bin/chromium'

# driver = webdriver.Chrome(service=ChromeDriverManager().install(),options=options)
driver = webdriver.Chrome()
driver.get("https://www.filmweb.pl/ranking/person/actors/male")
# waiting to load everything we need
elem = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.CLASS_NAME, "rankingTypePerson"))
)
soup = BeautifulSoup(driver.page_source, 'html.parser')

ranking_elements = soup.find_all(class_="rankingTypePerson")
for elem in ranking_elements:
    actor = {"name": elem.find(class_="rankingTypePerson__title").text, 
        # taking 1 element, because 0 one is with current photo, which is harder to recognize for me
          "image": elem.find_all("img")[1].attrs['src'], "url": elem.find(class_="rankingTypePerson__title").attrs['href']}
    actor["short_name"] = '_'.join(actor["name"].split()[1:]).lower()
    print(actor["short_name"])
    lines = ["---\nlayout: actor\n"]
    for key,value in actor.items():
        lines.append(f"{key}: {value}\n")
    lines.append("---\n")
    new_url = f"https://www.filmweb.pl{actor['url']}"
    lines.append(f"[link do filmweba]({new_url}) - źródło danych\n\n")

    driver.get(new_url)
    # waiting to load everything we need
    elem = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "personKnownFor__productionLink"))
    )
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    lines.append("## Lista filmów, z których jest znany:\n")
    films = soup.find_all(class_="personKnownForItem")
    for film in films:
        film_desc = film.find(class_="personKnownFor__productionLink")
        url = film_desc.attrs['href']
        film_name = film_desc.text
        film_image = film.find('img').attrs['src']
        # film_image = DDGS().images(keywords=f"{actor["name"]} {film_name}")[0].get("image")
        lines.append(f"- [{film_name}](https://www.filmweb.pl{url})\n![]({film_image})\n")

    lines.append("\n\n## linki do stron znalezione przez kaczkę:\n")
    # wait to not scare duck so it doesn't think we overuse it
    time.sleep(2.5)
    for url in DDGS().text(keywords=f"{actor["name"]}",max_results=2):
        title = url.get("title")
        href = url.get("href")
        lines.append(f"- [{title}]({href})\n")

        
    with open(f"_actors/{actor["short_name"]}.md", "w") as f:
        f.writelines(lines)
    