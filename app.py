import streamlit as st
import joblib
from datetime import datetime
import uuid

st.set_page_config(page_title="Quirkr - Smart Task Sorter", page_icon="🧠", layout="centered")

# Load trained ML model
model = joblib.load("ml/model.pkl")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.markdown("""
    <h1 style='text-align: center; color: #6A1B9A;'>🔮 Quirkr</h1>
    <h4 style='text-align: center;'>Smart Task Organizer</h4>
""", unsafe_allow_html=True)

with st.expander("➕ Add a New Task", expanded=True):
    task_input = st.text_input("Task description", placeholder="Type your task here...")
    if st.button("Add Task", use_container_width=True):
        if task_input:
            category = model.predict([task_input])[0]
            task_id = str(uuid.uuid4())[:8]
            st.session_state.tasks.append({
                "id": task_id,
                "task": task_input,
                "category": category,
                "done": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success(f"✅ Task added! Predicted Category: `{category}`")
        else:
            st.warning("⚠️ Task can't be empty!")

st.markdown("---")
st.subheader("📋 Your Quirkr Tasks")
if not st.session_state.tasks:
    st.info("No tasks added yet.")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3, col4 = st.columns([6, 2, 2, 1])
        with col1:
            status_icon = "✅" if task["done"] else "🕒"
            st.markdown(f"**{status_icon} {task['task']}**")
            st.caption(f"Category: `{task.get('category', 'None')}` | Created: {task.get('created_at', 'Unknown')}`")

        with col2:
            if st.button("Done ✅", key=f"done_{task['id']}"):
                st.session_state.tasks[i]["done"] = True
                st.rerun()
        with col3:
            if st.button("Delete 🗑️", key=f"delete_{task['id']}"):
                st.session_state.tasks.pop(i)
                st.rerun()
        st.markdown("---")