user_prompt = "Enter a todo: "  # type str
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]  # type list
# print(todos)  # type Function

# print(type(todos), type(user_prompt))
# todos = []
# while True:
#     todo = input(user_prompt)
#     capitalized = todo.capitalize() # title(), upper(), lower(),
#     print(capitalized)
#     todos.append(capitalized)
#     print(todos)

# password = input("Enter your password: ")
# while password != "12345":
#     password = input("Enter your password: ")

# print("Password is correct")

# x = 0
# while x <= 6:
#     print(x + 1)
#     x += 1

todos = []

while True:
    user_action = input("Enter add, view or exit: ").strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "view" | "display":  # Bitwise OR operator |
            for todo in todos:
                print(todo)
        case "exit":
            break
        case _:  # execute this line when none of the case is matched
            print("You entered a wrong command")
print("Bye :)")
