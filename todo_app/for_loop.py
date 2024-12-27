meals = ["rice", "pizza", "beans"]

################################

# for meal in meals:
#     for char in meal:
#         print(f"{char.title()} in {meal.capitalize()}")
#         if meal.endswith(char):
#             print()

# print("Done.")

################################

# meals.sort()  # sort method doesn't return an output
# meals.sort(reverse=True)  # sort method to reverse in descending order

# for i, meal in enumerate(meals):
#     row = f"{i + 1}.{meal.capitalize()}"
#     print(row)

# filenames = (
#     "1.first.txt",
#     "2.second.txt",
#     "3.third.txt",
# )  # tuple are immutable, while list are mutable

# for filename in filenames:
#     filename = filename.replace(".", "-", 1)
#     print(filename)

################################

# contents = [
#     "All carots are to be sliced longitudinally",
#     "The carrots were reportedly sliced",
#     "Carrots are ready to be eaten.",
# ]

# filenames = ["doc.txt", "reporter.txt", "presentation.txt"]

# for content, filename in zip(contents, filenames):
#     file = open(f"files/{filename}", "w")
#     file.write(content)

################################

filenames = ["1.doc", "2.reporter", "3.presentation"]

filenames = [
    filename.replace(".", "-") + ".txt" for filename in filenames
]  # list comprehension

print(filenames)
