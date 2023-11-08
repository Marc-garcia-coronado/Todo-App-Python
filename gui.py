import functions
import PySimpleGUI as sg
import time

sg.theme(new_theme="Gray")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="itemsTodos",
                      enable_events=True, size=(45, 10))
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")
exit_btn = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[
                        [clock],
                        [label],  # This is a row in the program
                        [input_box, add_btn],
                        [list_box],
                        [edit_btn, complete_btn],
                        [exit_btn]
                   ],
                   font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['itemsTodos'].update(values=todos)  # Update the list
            # print(todos)

        case "Edit":
            try:
                todo_to_edit = values['itemsTodos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['itemsTodos'].update(values=todos)  # Update the list

            except IndexError:
                sg.popup("Please select an item first!")

        case "Complete":
            try:

                todo_to_complete = values["itemsTodos"][0]

                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                # todos.remove(todo_to_complete) <- also correct
                functions.write_todos(todos)
                window['itemsTodos'].update(values=todos)  # Update the list

            except IndexError:
                sg.popup("Please select an item first!")

        case sg.WIN_CLOSED:
            break

        case "Exit":
            break

window.close()
