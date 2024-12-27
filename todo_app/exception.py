try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That is a square!")

    area = width * length
    print(f"Area of rectangle is {area}")

except ValueError:
    print("Please enter a number.")
