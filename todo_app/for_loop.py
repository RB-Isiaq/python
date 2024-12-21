meals = ["beans", "rice", "pizza"]

for meal in meals:
    for char in meal:
        print(f"{char.title()} in {meal.capitalize()}")
        if meal.endswith(char):
            print()

print("Done.")
