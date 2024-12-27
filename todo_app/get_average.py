def get_average(filepath):
    with open(filepath) as f:
        data = f.readlines()
    values = data[1:]
    values = [float(x) for x in values]

    avg = sum(values) / len(values)
    return avg


average = get_average("files/data.txt")
print(f"average is {average}")

feet_inches = input("Enter feet and inches: ")

# Decoupling is separting a single function to multiple functions, each doing a single task


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


f, i = parse(feet_inches)
result = convert(f, i)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slides")
