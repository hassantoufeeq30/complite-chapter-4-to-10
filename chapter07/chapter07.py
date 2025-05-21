# 7-1
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")

# 7-2
people = int(input("How many people are in your dinner group? "))
if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
# 7-4
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")

# 7-5
while True:
    age = int(input("Enter your age (or type 'quit' to exit): "))
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
# 7-6
# Version 1: Conditional test in the while statement
topping = ""
while topping != 'quit':
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

# Version 2: Active variable to control loop
active = True
while active:
    age = int(input("Enter your age (or type 'quit' to exit): "))
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
    continue_input = input("Do you want to continue? (yes/no): ")
    if continue_input == 'no':
        active = False

# Version 3: Using break statement
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")

# 7-7
while True:
    print("This loop will never end. Press ctrl-C or close the window to stop it.")
# 7-8
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'ham']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9
sandwich_orders = ['tuna', 'pastrami',
                   'chicken', 'pastrami', 'ham', 'pastrami']
print("We're sorry, but we're out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\nUpdated sandwich orders:")
for sandwich in sandwich_orders:
    print(sandwich)

# 7-10
vacation_poll = {}
while True:
    name = input("What is your name? ")
    destination = input(
        "If you could visit one place in the world, where would you go? ")
    vacation_poll[name] = destination
    repeat = input("Would you like to add another response? (yes/no): ")
    if repeat == 'no':
        break
print("\nPoll Results:")
for name, destination in vacation_poll.items():
    print(f"{name} would like to visit {destination}.")
