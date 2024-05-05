class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Task ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def is_valid_task_id(self, task_id):
        try:
            int(task_id)
            return True
        except:
            return False

    def is_valid_status(self, status):
        return status in ("Pending", "In Progress", "Completed")

    def is_valid_priority(self, priority):
        return priority in ("High", "Medium", "Low")

    def add_task(self, task_id, title, description, priority, status):
        if not self.is_valid_task_id(task_id):
            print("Task id must be a number.")
            return

        if not self.is_valid_priority(priority):
            print("Task priority value must be in (High, Medium, Low)")
            return

        if not self.is_valid_status(status):
            print("Task priority value must be in (Pending, In Progress, Completed).")
            return

        task = Task(task_id, title, description, priority, status)
        self.tasks.append(task)
        print("Task added successfully.")

    def edit_task(self, task_id, title, description, priority, status):
        if not self.is_valid_task_id(task_id):
            print("Task id must be a number.")
            return

        for task in self.tasks:
            if task.id == task_id:
                if title:
                    task.title = title

                if description:
                    task.description = description

                if priority:
                    if not self.is_valid_priority(priority):
                        print("Task priority value must be in (High, Medium, Low)")
                        return

                    task.priority = priority

                if status:
                    if not self.is_valid_status(status):
                        print(
                            "Task priority value must be in (Pending, In Progress, Completed)."
                        )
                        return

                    task.status = status

                print("Task edited successfully.")
                return

        print("Task not found.")

    def delete_task(self, task_id):
        if not self.tasks:
            print("Add Some Task First to delete.")
            return

        if not self.is_valid_task_id(task_id):
            print("Task id must be a number.")
            return

        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return

        print("Task not found.")

    def get_task_by_id(self, task_id):
        if not self.is_valid_task_id(task_id):
            print("Task id must be a number.")
            return

        for task in self.tasks:
            if task.id == task_id:
                print(task)
                return
        print("Task not found.")

    def view_all_tasks(self):
        if not self.tasks:
            print("You don't have any tasks.")
            return

        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        if not self.is_valid_priority(priority):
            print("Task priority value must be in (High, Medium, Low).")
            return

        filtered_tasks = []

        for task in self.tasks:
            if task.priority == priority:
                filtered_tasks.append(task)

        if filtered_tasks:
            for task in filtered_tasks:
                print(task)
        else:
            print("No tasks found with the specified priority.")


def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task_id = input("Enter task ID: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            task_manager.add_task(task_id, title, description, priority, status)
        elif choice == "2":
            task_id = input("Enter task ID to edit: ")
            title = input("Enter new title (leave blank to keep existing): ")
            description = input("Enter new description (leave blank to keep existing): ")
            priority = input("Enter new priority (leave blank to keep existing): ")
            status = input("Enter new status (leave blank to keep existing): ")
            task_manager.edit_task(task_id, title, description, priority, status)
        elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)
        elif choice == "4":
            task_manager.view_all_tasks()
        elif choice == "5":
            priority = input("Enter priority to filter tasks (High/Medium/Low): ")
            task_manager.filter_tasks_by_priority(priority)
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
