# 5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("Is fruit == 'banana'? I predict False.")
print(fruit == 'banana')

number = 10
print("Is number == 10? I predict True.")
print(number == 10)

print("Is number != 10? I predict False.")
print(number != 10)

name = 'Alice'
print("Is name == 'Alice'? I predict True.")
print(name == 'Alice')

print("Is name == 'alice'? I predict False.")
print(name == 'alice')

language = 'Python'
print("Is language == 'Python'? I predict True.")
print(language == 'Python')

print("Is language == 'Java'? I predict False.")
print(language == 'Java')

# 5-2
# Equality and inequality with strings
city = 'New York'
print(city == 'New York')
print(city != 'New York')

# Using lower()
print(city.lower() == 'new york')
print(city.lower() == 'NEW YORK')

# Numerical tests
age = 25
print(age == 25)
print(age != 30)
print(age > 20)
print(age < 30)
print(age >= 25)
print(age <= 24)

# and / or
print(age > 20 and age < 30)
print(age > 30 or age < 20)

# in list
colors = ['red', 'blue', 'green']
print('red' in colors)
print('yellow' in colors)

# not in list
print('black' not in colors)
print('blue' not in colors)

# 5-3 (passes the if test)
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points.")

# 5-3 (fails the if test)
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points.")
else:
    print("You just earned 0 points.")
# 5-4
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points.")
elif alien_color == 'yellow':
    print("You just earned 10 points.")
elif alien_color == 'red':
    print("You just earned 15 points.")
else:
    print("You just earned 0 points.")
    # 5-5 - version 1 (green)
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# 5-5 - version 2 (yellow)
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# 5-5 - version 3 (red)
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")
# 5-6
age = 30
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 5-7
favorite_fruits = ['banana', 'mango', 'apple']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")
# 5-8
usernames = ['admin', 'jaden', 'maria', 'leo', 'emma']
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
# 5-9
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10
current_users = ['John', 'Alice', 'Mike', 'Rachel', 'Sophie']
new_users = ['mike', 'sophie', 'Tom', 'Lily', 'George']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"Username '{new_user}' is already taken, please choose a different one.")
    else:
        print(f"Username '{new_user}' is available.")

# 5-11
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
