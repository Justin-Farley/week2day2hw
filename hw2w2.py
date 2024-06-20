# mytuple = [("Alice", "New York", "London"),("Bob", "Tokyo", "San Fransico")]
# name1, city1, city2 = mytuple[0]

# print(f"Itinerary 1: {name1} from {city1} to {city2}")

# name2, city3, city4 =mytuple[1]
# print(f"Itinerary 2: {name2} from {city3} to {city4}")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

found_1984 = False
found_BraveNewWorld = False

for book in library:
    print(book)
    if book[0] == "1984":
        found_1984 = True
    elif book[0] == "Brave New World":
        found_BraveNewWorld = True

print("Found '1984' in library:", found_1984)
print("Found 'Brave New World' in library:", found_BraveNewWorld)

new_book = ("Enders Game", "Orson Scott Card")
library.append(new_book)
print("Updated library:")
for book in library:
    print(book)



