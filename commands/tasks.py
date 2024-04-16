import os.path
import json
from datetime import datetime

FILE_NAME = 'tasks.json'

def show_tasks(args):
  with open(FILE_NAME, 'r') as tasks_json:
    try:
      data = json.load(tasks_json)
      for index, todo_task in enumerate(data.keys()):
        print(index + 1, data[todo_task]['title'])
    except:
      print('Some error occurred!')

def use_task(args):
  task_name = args[0]
  with open(FILE_NAME, 'r') as tasks_json:
    try:
      data = json.load(tasks_json)
      if (data.get(task_name)):
        return f'{task_name}.json'
      else:
        return -1
    except:
      print('Some error occurred!')

def create_task(args):
  task_name = args[0]
  # print(os.path.abspath('.'))
  new_task = {}
  with open(FILE_NAME, 'r+') as tasks_json:
    try:
      data = json.load(tasks_json)
      # print(data)
      # check if file already exists
      if (data.get(task_name)):
        print('Task already exists! Try a different name...')
      else:
        # update the new_task dict
        new_task = {
        'title': task_name,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        data[task_name] = new_task
        with open(f'tasks/{task_name}.json', 'w') as new_task:
          # empty task
          new_task.write('[\n]')
          print('Successfully created the new task!')
        # add to the tasks.json
        tasks_json.seek(0)
        json.dump(data, tasks_json, sort_keys=True, indent=True)
    except:
      print('Some error occurred!')





def remove_task(args):
  task_name = args[0]

  with open(FILE_NAME, 'r') as tasks_json:
    try:
      data = json.load(tasks_json)
      if (data.get(task_name)):
          with open(f'tasks/{task_name}.json', 'w') as remove_task:
             remove_task.write('[\n]')
          del data[task_name]
          with open(FILE_NAME, 'w') as tasks_json:
            json.dump(data, tasks_json, sort_keys=True, indent=True)
          
          print('Successfully remove the task!')
      else:
         print('Please select a correct task before this action')
    except:
      print('Some error occurred!')

