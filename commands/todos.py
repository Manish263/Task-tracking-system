import json
from datetime import datetime

def set_task(task_name):
  if (task_name == ''):
    print('Please select a given task before this action')
  return task_name

def get_data(task_file_name):
  """
  Get the deserialized data from the todo task json file
  """
  with open(f'tasks/{task_file_name}', 'r') as json_file:
    data = json.load(json_file)
  return data

def update_data(task_file_name, new_data):
  """
  Update the content of the todo task json file
  with the serialized version of 'new_data'
  """
  with open(f'tasks/{task_file_name}', 'w') as json_file:
    json.dump(new_data, json_file, sort_keys=True, indent=True)

def add_item(args):
  """
  Adds a todo item to the todo task
  """
  task_name = set_task(args[0])
  if (not task_name):
    return
  title = args[1]
  data = get_data(task_name)
  new_todo = {
    'title': title,
    'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    'completed': False
  }
  data.append(new_todo)
  update_data(task_name, data)

def show_items(args):
  """
  Prints all the todo items in the currently chosen todo task
  """
  task_name = set_task(args[0])
  if (not task_name):
    return
  data = get_data(task_name)
  complete = 0
  if (len(data) == 0):
    print('No todos in the task, why dont you add one?')
  else:
    for index, todo_item in enumerate(data):
      print(index + 1, todo_item['title'])
      if (todo_item['completed']):
        complete += 1
    print(f'{complete}/{len(data)} completed!')

def edit_item(args):
  """
  Edit a particular todo item
  """
  task_name = set_task(args[0])
  if (not task_name):
    return
  item_id = int(args[1])
  new_title = args[2]
  data = get_data(task_name)
  updated_todo = {
    'title': new_title,
    'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    'completed': False
  }
  data[item_id - 1] = updated_todo
  update_data(task_name, data)

def remove_item(args):
  """
  Remove a todo item
  """
  task_name = set_task(args[0])
  if (not task_name):
    return
  item_id = int(args[1])
  data = get_data(task_name)
  data.pop(item_id - 1)
  update_data(task_name, data)

def complete_item(args):
  """
  Mark a todo item as completed
  """
  task_name = set_task(args[0])
  if (not task_name):
    return
  item_id = int(args[1])
  data = get_data(task_name)
  data[item_id - 1]['completed'] = True
  update_data(task_name, data)

def incomplete_item(args):
  """
  Mark a todo item as incomplete
  """
  task_name = set_task(args[0])
  if (not task_name):
    return
  item_id = int(args[1])
  data = get_data(task_name)
  data[item_id - 1]['completed'] = False
  update_data(task_name, data)