tasks = []
print ("Welcome to Your Personal Task Manager!")

while True:
  print("What would you like to do?")
  print("1 - Add a task")
  print("2 - Remvoe a task")
  print("3 - Clear all tasks")
  print("4 - Exit")

user_choice = input("Enter your choice (1-4): ")

if user_choice == "1":
  new_task = input("Enter the task to add: ")
  tasks.append(new_task)
  print(f"'{new_task}' has been added to your list.")
  print(f"Current tasks: {tasks}")
elif user_choice == "2":
    if tasks == []:
        print("Your task list is empty!")
  else:
      task_to_remove = input("Enter the task to remove:)

      if task_to_remove in tasks:
           tasks.remove(task_to_remove)
            print(f"'{task_to_remove}' has been removed from your list.")
                             else:
                                  print(f"Current tasks: {tasks}") 

elif user_choice == "3":
    if tasks == []:
        print("Your task list is already empty!")
    else:
        tasks.clear()
        print("All tasks have been cleared!")

elif user_choice == "4":
    print("Thank you for using Your Personal Task Manager! Goodbye!")
    break

else:
    print("Invalid choice! Please enter a number between 1-4.")







      
                
