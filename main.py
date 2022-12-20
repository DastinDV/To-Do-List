from functions import get_todos,write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n";

        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos(todos, "todos.txt")
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            removed = todos[number-1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos, "todos.txt")

            message = f"Todo {removed} was removed from the list!"
            print(message)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            print('Here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, "todos.txt")
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("exit"):
        break;
    else:
        print('Hey! it is uknown command')