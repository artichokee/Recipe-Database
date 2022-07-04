# Scrape initialization
import requests
import bs4

base_url = input("Enter recipe URL: ")
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, "lxml")

modification =  input("Enter recipe modifications: ")

# Recipe name
recipe_soup = soup.find('h2', {'itemprop': 'name'})
recipe_name = recipe_soup.text
print(f"Name: {recipe_name}")

# Recipe Image
recipe_soup = soup.find('img', {'itemprop': 'image'})
recipe_image = recipe_soup.get('src')
print(f"Image Link: {recipe_image}")

# Prep Time
recipe_soup = soup.find('time', {'itemprop': 'prepTime'})
recipe_prep = recipe_soup.text
print(f"Prep Time: {recipe_prep}")

# Cook Time 
recipe_soup = soup.find('time', {'itemprop': 'totalTime'})
recipe_cook = recipe_soup.text
print(f"Cook Time: {recipe_cook}")

# Servings
recipe_soup = soup.find_all('p', {'itemprop': 'recipeIngredient'})
recipe_servings = ''.join(filter(str.isdigit, recipe_soup[0].text))
print(f"Servings: {recipe_servings}")

# Ingredients
recipe_ingredient = recipe_soup[1].text
recipe_ingredients = recipe_ingredient.split('\n')
print("Ingredients:")
for i,ingredient in enumerate(recipe_ingredients):
    print(f'{ingredient}')

print(f"Modification: {modification}")

