class Task:
    """Class to represent a task"""
    def __init__(self, description, status='Not Completed'):
        self.description = description
        self.status = status

    def mark_completed(self):
        self.status = 'Completed'

    def __str__(self):
        return f"Task: {self.description}, Status: {self.status}"


class ToDoList:
    """Class to represent a To-Do List"""
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def edit_task(self, task_index, new_description):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
            print("Task added successfully.")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index: "))
            new_description = input("Enter new task description: ")
            todo_list.edit_task(task_index, new_description)
            print("Task edited successfully.")
        elif choice == '4':
            task_index = int(input("Enter task index: "))
            todo_list.delete_task(task_index)
            print("Task deleted successfully.")
        elif choice == '5':
            print("Thank you for using the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
