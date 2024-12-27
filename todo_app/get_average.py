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


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slides")
