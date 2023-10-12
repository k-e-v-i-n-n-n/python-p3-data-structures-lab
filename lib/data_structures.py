import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = [key["name"] for key in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spicy_dict = []

    for food in spicy_foods:
        if food["heat_level"] > 5:
            spicy_dict.append(food)
    return spicy_dict

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        formatted = f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
        print(formatted)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for food in spicy_foods:
        if food["cuisine"] == cuisine:
                return food
    

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            formatted = f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
            print(formatted)

def get_average_heat_level(spicy_foods):

    total = 0
    elements = len(spicy_foods)

    for food in spicy_foods:
        total += food["heat_level"]
    
    average = total / elements
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
