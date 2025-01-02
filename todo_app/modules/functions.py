def get_todos(filepath="files/todos.txt"):
    """Read a text file and return a list of todo items."""  # Documentation strings - Docstrings
    with open(filepath, "r") as file:  # using with-context manager
        todos = file.readlines()
    return todos


# print(help(get_todos))


def write_todos(todos_arg, filepath="files/todos.txt"):
    """Write and save todo items to a text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if (
    __name__ == "__main__"
):  # This will only run when this file is executed, and not when imported in another file.
    print(get_todos())
