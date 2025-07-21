import streamlit as st
import joblib

# Load trained ML model
model = joblib.load("ml/model.pkl")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("🧠 Quirkr - Smart To-Do App")

# Input box for task
task_input = st.text_input("➕ Add a new task")

if st.button("Add Task"):
    if task_input:
        category = model.predict([task_input])[0]
        st.session_state.tasks.append({
            "task": task_input,
            "category": category,
            "done": False
        })
        st.success(f"Task added! ✅ Category: {category}")
    else:
        st.warning("Task can't be empty!")

# Display tasks
st.markdown("## 📝 Your To-Do List")
if not st.session_state.tasks:
    st.info("No tasks added yet.")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([6, 1, 1])
        with col1:
            status = "✅" if task["done"] else "⏳"
            st.write(f"**{status} {task['task']}**")
            st.caption(f"Category: `{task['category']}`")
        with col2:
            if st.button("Done", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = True
        with col3:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
