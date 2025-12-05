to_do = []
completed = []

def add():
    new = input("Add task: ").strip()
    if new:
        to_do.append(new)
        print(f'Added: "{new}"')
    else:
        print("ENTER A TASK")

def remove():
    if not to_do:
        print("No tasks to remove")
        return
    show_list()
    rem = input ("What task should we remove? ").strip()
    if rem in to_do:
        to_do.remove(rem)
        print(f'Removed: "{rem}"')
    else:
        print(f'"{rem}" not found in your list.')

def edit():
    if not to_do:
        print("No tasks to edit")
        return
    show_list()
    original = input("Which task would you like to change? ").strip()
    if original in to_do:
        index = to_do.index(original)
        changed = input("Enter the amended version: ").strip()
        if changed:
            to_do[index] = changed 
            print(f'Updated: "{original}" to "{changed}"')
        else:
            print("Task has been repeated. Edit removed.")
    else:
        print(f'"{original}" not found.')

def mark_done():
    if not to_do:
        print("No tasks accessilbe")
        return
    show_list()
    done = input("Which task has been complete? ").strip()
    if done in to_do:
        to_do.remove(done)
        completed.append(done)
        print(f'Marked as completed: "{done}"')
    else:
        print(f'"{done}" not found.')

def show_list():
    if not to_do:
        print("No tasks accessible")
    else:
        print("Your task list:")
        for i, task in enumerate(to_do, 1):
            print(f"{i}. {task}")
        print()

def show_completed():
    if not completed: 
        print("No completed tasks")
    else:
        print("Completed tasks:")
        for i, task in enumerate(completed, 1):
            print(f"{i}. {task}")
        print()

def clear_all():
    to_do.clear()
    completed.clear()
    print("All tasks removed")

def main_menu():
    print("How Can I Help You Today?")
    print("1. Add new tasks")
    print("2. Remove tasks")
    print("3. Edit existing tasks")
    print("4. Mark tasks as completed")
    print("5. Display all tasks")
    print("6. Display all completed tasks")
    print("7. Remove all tasks")
    print("8. Exit the application")

def main():
    while True:
        main_menu()
        choice = input("> ").strip()

        if choice == '1':
            add()
        elif choice == '2':
            remove()
        elif choice == '3':
            edit()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            show_list()
        elif choice == '6':
            show_completed()
        elif choice == '7':
            clear_all()
        elif choice == '8':
            print("Have a Great Rest of Your Day!")
            break
        else:
            print("Invaled input. Pick 1-8")
main()
    
