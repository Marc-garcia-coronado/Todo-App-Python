from functions import get_todos, write_todos, show_todos

if __name__ == '__main__':

    local_todos = get_todos(filepath="todos.txt")

    while True:

        print("What do you want to do?")
        user_input = input("Options -> add, show, edit, complete, save or exit: ")
        user_input = user_input.split(None, 1)
        user_action = user_input[0]
        user_todo = user_input[1] if len(user_input) > 1 else ""

        if user_action == "add":

            local_todos.append(user_todo)

        elif user_action == "show":

            new_todos = []

            for item in local_todos:
                new_item = item.strip("\n")
                new_todos.append(new_item)

            show_todos(new_todos)
            # Calling show_todos to show the actual todos that we have via this function

        elif user_action == "edit" and len(user_input) > 1:

            if len(local_todos) > 0:

                edit_todo_index = int(user_todo) - 1
                new_edited_todo = input("Write the new todo -> ")
                print(f"Edited ({local_todos[edit_todo_index].strip()}) --> ({new_edited_todo}):")
                local_todos[edit_todo_index] = new_edited_todo

            else:
                print("You don't have any todo to edit!")

        elif user_action == "complete" and len(user_input) > 1:

            completed_todo = int(user_todo) - 1
            todo_to_remove = local_todos[completed_todo].strip("\n")
            local_todos.pop(completed_todo)

            write_todos(local_todos)
            print(f"Todo ({todo_to_remove}) has been removed!")

        elif user_action == "save":

            write_todos(local_todos)

        elif user_action == "exit":
            break

        else:
            print(f"Command ({user_action}) NOT FOUND or MISSING some parameter!")
