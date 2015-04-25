todos = []

def add_todo(item):
    todos.append(item)
    return "{} has been added to your to-do list.".format(item)

def list_todos():
    return "Your to-do list contains " + \
        ", ".join(todos[:-2] + [" and ".join(todos[-2:])])
