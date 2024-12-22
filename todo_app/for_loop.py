meals = ["beans", "rice", "pizza"]

for meal in meals:
    for char in meal:
        print(f"{char.title()} in {meal.capitalize()}")
        if meal.endswith(char):
            print()

print("Done.")

# filenames = (
#     "1.first.txt",
#     "2.second.txt",
#     "3.third.txt",
# )  # tuple are immutable, while list are mutable

# for filename in filenames:
#     filename = filename.replace(".", "-", 1)
#     print(filename)
