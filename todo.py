import streamlit as st

# Title of the application
st.title("To-Do List")

# Create a session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a task
def add_task(task):
    st.session_state.tasks.append(task)

# Function to remove a task
def remove_task(index):
    del st.session_state.tasks[index]

# Input field for adding a new task
new_task = st.text_input("Enter a new task:")

# Button to add the new task
if st.button("Add Task"):
    if new_task:
        add_task(new_task)
        st.success(f"Task '{new_task}' added!")
        st.experimental_rerun()  # Refresh to show the updated list
    else:
        st.error("Please enter a task.")

# Display the list of tasks
if st.session_state.tasks:
    st.subheader("Your Tasks")
    for idx, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{idx + 1}. {task}")
        with col2:
            if st.button("Remove", key=idx):
                remove_task(idx)
                st.experimental_rerun()  # Refresh to show the updated list
else:
    st.write("No tasks yet!")

# Footer
st.write("Powered by Streamlit")
