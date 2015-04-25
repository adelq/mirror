todos = []

def add_todo(item):
    todos.append(item)

def list_todos():
    print "Your todo list contains " + \
        ", ".join(todos[:-2] + [" and ".join(todos[-2:])])
