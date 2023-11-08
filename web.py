import streamlit as st
import functions

# To run this program type in the terminal the following command
# streamlit run web.py

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_todos(todos)


st.header("My Todo App")
st.subheader("This is my todo app!")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=i)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(placeholder="Enter a todo...", label="Enter a todo:", on_change=add_todo,
              key="new_todo")
