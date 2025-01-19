tasks=[]

def add_tasks():
  task = input("Enter a new task: ")
  tasks.append(task)
  print("Task added!")
  
def view_tasks():
  if len(tasks) == 0:
    print("No tasks available.")
  else:
    print("Your tasks are:")
    for i, task in enumerate(tasks):
      print(f'{i+1}. {task}')

def delete_task():
  if len(tasks) == 0:
    print("No tasks available.")
  else:
    print('Before deletion your tasks are:')
    for i, task in enumerate(tasks):
      print(f'{i+1}. {task}')
    choice = int(input('Enter the task number to delete: '))
    
    if 0 < choice <= len(tasks):
      del tasks[choice - 1]
      print("Task deleted!")
          
    else:
      print("Invalid task number.")
      
def update_tasks():
  print('Your updated current tasks:')
  for i, task in enumerate(tasks):
    print(f'{i+1}. {task}')
     
def main():
  while True:
    print("\n Task Manager Menu:")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Update a task")
    print("5. Quit")
  
    choice = int(input("Enter your choice: "))
    if choice == 1:
      add_tasks()
    elif choice == 2:
      view_tasks()
    elif choice == 3:
      delete_task()
    elif choice == 4:
      update_tasks()
    elif choice == 5:
      print("This is todo list application tasks, exit")
      break
    else:
      print("Goodbye try next time to enter the task list! As you entered input is Invalid detail")
      
if __name__=="__main__":
  main()