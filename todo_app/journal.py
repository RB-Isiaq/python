date = input("Enter today's date: ")
mood = input("How do you rate your mood from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"files/journals/{date}.txt", "w") as file:
    file.write(f"({mood} *)" + 2 * "\n")
    file.write(thoughts)
