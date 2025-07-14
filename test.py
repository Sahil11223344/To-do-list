import streamlit as st

def main():
    st.set_page_config(page_title="Task Management App", page_icon="📝", layout="centered")
    
    st.title("📝 Task Management App")
    st.markdown("---")
    
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []
    
    # Sidebar for operations
    st.sidebar.header("Operations")
    operation = st.sidebar.selectbox(
        "Choose an operation:",
        ["Add Task", "Update Task", "Delete Task", "View Tasks", "Clear All Tasks"]
    )
    
    if operation == "Add Task":
        st.header("➕ Add New Task")
        
        if st.checkbox("Add multiple tasks at once"):
            num_tasks = st.number_input("How many tasks do you want to add?", min_value=1, max_value=10, value=1)
            
            new_tasks = []
            for i in range(num_tasks):
                task = st.text_input(f"Enter task {i+1}:", key=f"task_{i}")
                if task:
                    new_tasks.append(task)
            
            if st.button("Add All Tasks"):
                for task in new_tasks:
                    if task and task not in st.session_state.tasks:
                        st.session_state.tasks.append(task)
                if new_tasks:
                    st.success(f"Added {len(new_tasks)} tasks successfully!")
        else:
            # Single task addition
            new_task = st.text_input("Enter task you want to add:")
            if st.button("Add Task"):
                if new_task:
                    if new_task not in st.session_state.tasks:
                        st.session_state.tasks.append(new_task)
                        st.success(f"Task '{new_task}' has been successfully added!")
                    else:
                        st.warning("Task already exists!")
                else:
                    st.error("Please enter a task!")
    
    elif operation == "Update Task":
        st.header("✏️ Update Task")
        
        if st.session_state.tasks:
            task_to_update = st.selectbox("Select task to update:", st.session_state.tasks)
            new_task_name = st.text_input("Enter new task name:")
            
            if st.button("Update Task"):
                if new_task_name:
                    if new_task_name not in st.session_state.tasks:
                        index = st.session_state.tasks.index(task_to_update)
                        st.session_state.tasks[index] = new_task_name
                        st.success(f"Task updated to '{new_task_name}'!")
                    else:
                        st.warning("Task with this name already exists!")
                else:
                    st.error("Please enter a new task name!")
        else:
            st.info("No tasks available to update. Add some tasks first!")
    
    elif operation == "Delete Task":
        st.header("🗑️ Delete Task")
        
        if st.session_state.tasks:
            task_to_delete = st.selectbox("Select task to delete:", st.session_state.tasks)
            
            if st.button("Delete Task", type="secondary"):
                st.session_state.tasks.remove(task_to_delete)
                st.success(f"Task '{task_to_delete}' has been deleted!")
        else:
            st.info("No tasks available to delete. Add some tasks first!")
    
    elif operation == "View Tasks":
        st.header("👀 View All Tasks")
        
        if st.session_state.tasks:
            st.subheader(f"Total tasks: {len(st.session_state.tasks)}")
            
            for i, task in enumerate(st.session_state.tasks, 1):
                st.write(f"{i}. {task}")
        else:
            st.info("No tasks available. Add some tasks first!")
    
    elif operation == "Clear All Tasks":
        st.header("🧹 Clear All Tasks")
        
        if st.session_state.tasks:
            st.warning(f"You have {len(st.session_state.tasks)} tasks. This action cannot be undone!")
            
            if st.button("Clear All Tasks", type="secondary"):
                st.session_state.tasks.clear()
                st.success("All tasks have been cleared!")
        else:
            st.info("No tasks to clear!")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Current Tasks")
    if st.session_state.tasks:
        for i, task in enumerate(st.session_state.tasks, 1):
            st.sidebar.write(f"{i}. {task}")
    else:
        st.sidebar.write("No tasks yet!")

if __name__ == "__main__":
    main()