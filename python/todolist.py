class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f'Task "{deleted_task}" deleted.')
        else:
            print('Invalid task index.')

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += ' (Completed)'
            print('Task marked as completed.')
        else:
            print('Invalid task index.')

    def display_tasks(self):
        if self.tasks:
            print('To-Do List:')
            for index, task in enumerate(self.tasks):
                print(f'{index + 1}. {task}')
        else:
            print('No tasks in the list.')

def main():
    todo_list = ToDoList()
    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. Delete Task')
        print('3. Mark Task as Completed')
        print('4. Display Tasks')
        print('5. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input('Enter the index of task to delete: ')) - 1
            todo_list.delete_task(task_index)
        elif choice == '3':
            task_index = int(input('Enter the index of task to mark as completed: ')) - 1
            todo_list.mark_completed(task_index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()
