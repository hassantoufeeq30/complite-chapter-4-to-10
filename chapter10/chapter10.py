# 10-1
with open('learning_python.txt', 'r') as file:
    content = file.read()
    print(content)
    file.seek(0)
    for line in file:
        print(line.strip())
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# 10-2
with open('learning_python.txt', 'r') as file:
    for line in file:
        print(line.replace('Python', 'C').strip())
# 10-3
name = input("What is your name? ")
with open('guest.txt', 'w') as file:
    file.write(name)

# 10-4
while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break
    print(f"Hello, {name}!")
    with open('guest_book.txt', 'a') as file:
        file.write(f"{name}\n")

# 10-5
while True:
    reason = input("Why do you like programming? (Type 'quit' to exit) ")
    if reason.lower() == 'quit':
        break
    with open('programming_poll.txt', 'a') as file:
        file.write(f"{reason}\n")
# 10-6
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum is: {result}")
except ValueError:
    print("Please enter valid numbers.")

# 10-7
while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
        break
    except ValueError:
        print("Please enter valid numbers.")

# 10-8
try:
    with open('cats.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file cats.txt is missing.")

try:
    with open('dogs.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file dogs.txt is missing.")

# 10-9
try:
    with open('cats.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    pass

try:
    with open('dogs.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    pass

# 10-10
file_path = 'path_to_your_text_file.txt'

try:
    with open(file_path, 'r') as file:
        text = file.read()
        word_count = text.lower().count('the ')
        print(f"The word 'the' appears {word_count} times.")
except FileNotFoundError:
    print(f"The file {file_path} is missing.")
