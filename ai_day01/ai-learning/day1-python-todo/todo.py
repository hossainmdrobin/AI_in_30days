import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except:
        return []
def save_tasks(tasks):
    with open(FILE,"w") as f:
        json.dump(tasks,f)

def add_task(title):
    tasks = load_tasks()
    tasks.append({'title':title,'done':False})
    save_tasks(tasks)
    print("Task added")

def complete_task():
    index = int(input("enter task index: "))
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "✓" if task['done'] else " "
        print(f"{i+1}. [{status}] {task['title']}")
    
while True:
    print('\n1. Add Task')
    print('2. Lisk task')
    print('3. Complete task')
    print("4. exit")
    choice = input("Choose: ")


    if choice == "1":
        title = input("Task Title: ")
        add_task(title)

    elif choice == "2":
        list_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4": break