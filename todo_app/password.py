password = input("Enter your password: ")

# results = []
results = {}
if len(password) >= 8:
    # results.append(True)
    results["length"] = True
else:
    # results.append(False)
    results["length"] = False

isdigit = False
for i in password:
    if i.isdigit():
        isdigit = True

# results.append(isdigit)
results["is_digit"] = isdigit

isupper = False
for i in password:
    if i.isupper():
        isupper = True

# results.append(isupper)
results["is_upper"] = isupper

print(results)
print(results.values())

if all(results.values()):
    print("Strong password")
else:
    print("Weak password")
