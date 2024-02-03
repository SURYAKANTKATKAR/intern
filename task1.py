class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [t for t in self.tasks if t.name != task_name]

    def display_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.name}, Due Date: {task.due_date}, Priority: {task.priority}")
def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            task = Task(name, due_date, priority)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            name = input("Enter task name to remove: ")
            todo_list.remove_task(name)
            print("Task removed successfully!")

        elif choice == '3':
            print("Your To-Do List:")
            todo_list.display_tasks()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
