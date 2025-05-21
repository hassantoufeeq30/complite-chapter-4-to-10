# 6-1
person = {
    'first_name': 'Liam',
    'last_name': 'Taylor',
    'age': 28,
    'city': 'Toronto'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 13,
    'Charlie': 42,
    'Diana': 3,
    'Ethan': 27
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

# 6-3
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'A collection of items stored in a single variable.',
    'dictionary': 'A collection of key-value pairs.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
# 6-4
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'A collection of items stored in a single variable.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A sequence of characters.',
    'integer': 'A whole number, positive or negative.',
    'float': 'A number with a decimal point.',
    'boolean': 'A data type that can be either True or False.',
    'tuple': 'An ordered collection of elements that cannot be changed.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
# 6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())
# 6-7
person_1 = {
    'first_name': 'Liam',
    'last_name': 'Taylor',
    'age': 28,
    'city': 'Toronto'
}

person_2 = {
    'first_name': 'Emily',
    'last_name': 'Smith',
    'age': 34,
    'city': 'New York'
}

person_3 = {
    'first_name': 'Jack',
    'last_name': 'Jones',
    'age': 25,
    'city': 'London'
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"{person['first_name']} {person['last_name']}:")
    print(f"  Age: {person['age']}")
    print(f"  City: {person['city']}\n")
# 6-8
pet_1 = {
    'animal': 'dog',
    'owner': 'Alice'
}

pet_2 = {
    'animal': 'cat',
    'owner': 'Bob'
}

pet_3 = {
    'animal': 'parrot',
    'owner': 'Charlie'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner']} has a {pet['animal']}.\n")
# 6-9
favorite_places = {
    'Alice': ['Paris', 'Tokyo'],
    'Bob': ['New York'],
    'Charlie': ['London', 'Sydney', 'Berlin']
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are: {', '.join(places)}.\n")
# 6-10
favorite_numbers = {
    'Alice': [7, 14, 21],
    'Bob': [13, 26, 39],
    'Charlie': [42, 84, 126]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}.\n")
# 6-11
cities = {
    'Toronto': {
        'country': 'Canada',
        'population': 2800000,
        'fact': 'Toronto is the largest city in Canada.'
    },
    'New York': {
        'country': 'United States',
        'population': 8400000,
        'fact': 'New York is known for its skyscrapers.'
    },
    'London': {
        'country': 'United Kingdom',
        'population': 8900000,
        'fact': 'London is famous for its historical landmarks.'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
# 6-12
cities = {
    'Toronto': {
        'country': 'Canada',
        'population': 2800000,
        'fact': 'Toronto is the largest city in Canada.',
        'language': 'English and French',
        'landmark': 'CN Tower'
    },
    'New York': {
        'country': 'United States',
        'population': 8400000,
        'fact': 'New York is known for its skyscrapers.',
        'language': 'English',
        'landmark': 'Statue of Liberty'
    },
    'London': {
        'country': 'United Kingdom',
        'population': 8900000,
        'fact': 'London is famous for its historical landmarks.',
        'language': 'English',
        'landmark': 'Big Ben'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")
    print(f"  Language: {info['language']}")
    print(f"  Landmark: {info['landmark']}\n")
