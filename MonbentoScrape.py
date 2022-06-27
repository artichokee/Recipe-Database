# Scrape initialization
import requests
import bs4

base_url = input("Enter recipe URL: ")

res = requests.get(base_url)

soup = bs4.BeautifulSoup(res.text, "lxml")

# isolate section with name and recipe details
recipe = soup.select('.penci-recipe-metades')
header = recipe[0]

print(f"{header}")

recipe_name = header.find("span", itemprop="name")

print(f"{recipe_name}")
