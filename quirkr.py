import joblib

tasks = []  # List to store tasks

# Load the ML model
model = joblib.load("ml/model.pkl")

def add_task():
    task = input("Enter task description: ")
    category = model.predict([task])[0]  # Predict category using ML
    tasks.append({"task": task, "category": category, "done": False})
    print(f"Task added. Predicted category: {category}")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for idx, t in enumerate(tasks, 1):
            status = "Done" if t["done"] else "Pending"
            print(f"{idx}. [{status}] {t['task']} (Category: {t['category']})")

def mark_done():
    if not tasks:
        print("No tasks to mark.")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\nQUIRKR APP MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting Quirkr App.")
        break
    else:
        print("Invalid choice. Try again.")
