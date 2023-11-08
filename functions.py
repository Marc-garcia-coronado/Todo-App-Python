FILEPATH = "todos.txt"


def show_todos(todos_list):

    """
    Prints the todos_list via console
    :param todos_list:
    """

    if len(todos_list) > 0:
        [print(f"{i + 1} -> {todo}") for i, todo in enumerate(todos_list)]
    else:
        print("Seems that you don't have any todo yet!")


def write_todos(todos_list, filepath=FILEPATH):

    """
    Write the to-do items list in a text file from the todos_list
    :param todos_list:
    :param filepath:
    """

    try:
        with open(filepath, "w") as file:
            [file.write(f"{x.strip()}\n") for x in todos_list]

    except FileExistsError:
        print(FileExistsError)


def get_todos(filepath=FILEPATH) -> list:

    """
    Read a text file and reurn the list of to-do items.
    :param filepath:
    :return: list of to-do's of the file if its created
    """

    try:
        with open(filepath, "r") as f:
            todos_local = list(f.readlines())
            # Same as doing this above -> todos = [] and then inserting the todos in it

    except FileExistsError:
        print(FileExistsError)

    return todos_local


if __name__ == '__main__':
    print(get_todos(FILEPATH))
