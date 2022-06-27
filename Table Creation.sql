-- TODO: add foreign key

CREATE TABLE recipe (
    recipe_id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(100),
    modification VARCHAR(500)
)

CREATE TABLE secondary_info (
    secondary_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipe(recipe_id),
    prep_time VARCHAR(25),
    cooking_time VARCHAR(25),
    servings INTEGER(2)
)

CREATE TABLE ingredient (
    ingredient_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipe(recipe_id),
    ingredient_name VARCHAR(50)
)

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipe(recipe_id),
    tag_name VARCHAR(20)
)