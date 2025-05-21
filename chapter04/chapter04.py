# 4.1
pizzas = ["pepperoni", "margherita", "bbq chicken"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I enjoy all kinds of pizza.")
print("They are flavorful and satisfying.")
print("Pizza is my go-to comfort food.")
print("I really love pizza!")
# 4.2
animals = ["dog", "cat", "rabbit"]

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals would make a great pet!")

# 4-3
for number in range(1, 21):
    print(number)

# 4-4
numbers = list(range(1, 1_000_001))
# for number in numbers:
#     print(number)  # Uncomment to print all, but it's very slow

# 4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
for number in range(1, 21, 2):
    print(number)

# 4-7
for number in range(3, 31, 3):
    print(number)

# 4-8
cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
for cube in cubes:
    print(cube)

# 4-9
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

# 4-10
pizzas = ["pepperoni", "margherita", "bbq chicken", "veggie", "hawaiian"]

print("The first three items in the list are:")
print(pizzas[:3])

print("Three items from the middle of the list are:")
print(pizzas[1:4])

print("The last three items in the list are:")
print(pizzas[-3:])
# 4-11
pizzas = ["pepperoni", "margherita", "bbq chicken"]
friend_pizzas = pizzas[:]

pizzas.append("cheese")
friend_pizzas.append("mushroom")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12
foods = ["pizza", "falafel", "carrot cake"]

print("My favorite foods are:")
for food in foods:
    print(food)

friend_foods = ["sushi", "ice cream", "pasta"]

print("My friend’s favorite foods are:")
for food in friend_foods:
    print(food)
