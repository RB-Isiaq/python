user_prompt = "Enter a todo: "  # type str
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]  # type list
# print(todos)  # type Function

# print(type(todos), type(user_prompt))

# ---------------------

# todos = []
# while True:
#     todo = input(user_prompt)
#     capitalized = todo.capitalize() # title(), upper(), lower(),
#     print(capitalized)
#     todos.append(capitalized)
#     print(todos)

# ---------------------

# password = input("Enter your password: ")
# while password != "12345":
#     password = input("Enter your password: ")

# print("Password is correct")

# ---------------------

# x = 0
# while x <= 6:
#     print(x + 1)
#     x += 1

# ---------------------

# todos = []

while True:
    user_action = input("Enter add, view, edit, complete or exit: ").strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open(
                "files/todos.txt", "r"
            )  # relative path. for absolute paths on windows with backslashes, prefix it with r, to avoid the special characters and read it as a row string e.g open(r"C:\downloads\files\todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "view" | "display":  # Bitwise OR operator |
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]  # List comprehension

            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                row = f"{index + 1} - {todo}"
                print(row)
        case "edit":
            for todo in todos:
                print(todos.index(todo) + 1, todo)
            todo_index = int(input("Enter todo index: ")) - 1
            edit_todo = todos[todo_index]
            if edit_todo:
                edited_todo = input(f"Update this todo - {edit_todo}: ")
                todos[todo_index] = edited_todo
                print(f"{edit_todo} has been updated to: {edited_todo}")
        case "complete":
            todo_index = int(input("Enter todo index to complete: ")) - 1
            completed_todo = todos.pop(todo_index)
            print(f"{completed_todo} has been completed")

        case "exit":
            break
        case _:  # execute this line when none of the case is matched
            print("You entered a wrong command")
print("Bye :)")

# ---------------------


def greet(name):
    print(f"Hello world, my name is {name}")


greet("Ridwan")
