# 8.1
def dispaly_massage():
    print("in this chapter we will leraning in funcation .")


dispaly_massage()

# 8.2


def favorite_book(book_name):
    print(f"my favorite book is {book_name}")


favorite_book("alice in wonderland")
# 8.3


def make_shirt(size, text):
    print(f"the size of the shirt is {size} and the text on it is {text}")


make_shirt("large", "i love python")
make_shirt("medium", "i love python")
# 8.4


def make_shirt(size="large", text="i love python"):
    print(f"the size of the shirt is {size} and the text on it is {text}")


make_shirt()
make_shirt("medium")
make_shirt("small", "i love python")
make_shirt("large", "i love python")
# 8.5


def describe_city(city, country="iceland"):
    print(f"{city} is in {country}")


describe_city("reykjavik")
describe_city("akureyri")
describe_city("tokyo", "japan")
# 8.6


def city_country(city, country):
    return f"{city}, {country}"


print(city_country("reykjavik", "iceland"))
print(city_country("tokyo", "japan"))

# 8.7


def make_album(artist_name, album_title, tracks=None):
    album = {"artist": artist_name, "album": album_title}
    if tracks:
        album["tracks"] = tracks
    return album


print(make_album("artist1", "album1"))
print(make_album("artist2", "album2", 10))
# 8.8


def show_album(album):
    while True:
        print(album)
        break
    return album


album1 = make_album("artist1", "album1")
album2 = make_album("artist2", "album2", 10)
show_album(album1)
show_album(album2)
# 8.9


def show_massage(list):
    list = ["hello", "hi", "how are you"]
    for i in list:
        print(i)
    return list


list = ["hello", "hi", "how are you"]
show_massage(list)
# 8.10


def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

    return sent_messages


messages = ["Hello", "How are you?", "Goodbye"]
sent_messages = send_messages(messages[:])
print("\nSent messages:")
for message in sent_messages:
    print(message)
# 8.11


def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich("lettuce", "tomato", "turkey")

# 8.12


def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics")
print(user_profile)
# 8.13


def car_info(manufacturer, model, **car_info):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car = car_info("subaru", "outback", color="blue", tow_package=True)
print(car)
