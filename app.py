from commands import commands_dict1,commands_dict2

def parse(command):
  """
  Takes the command as input and returns the command name and args
  """
  cmd_task = command.split()
  cmd_type = cmd_task[0]
  if (cmd_type == 'help' or cmd_type == 'exit'):
    return cmd_type, cmd_task[1:]
  elif (cmd_type == 'task'):
    cmd_name = cmd_task[1]
    if (cmd_name in ['show', 'use', 'create', 'remove', ]):
      return cmd_name, cmd_task[2:]
    else:
      return 'invalid', []
  elif (cmd_type == 'todo'):
    cmd_name = cmd_task[1]
    if (cmd_name in ['add', 'all', 'edit', 'remove', 'complete', 'incomplete']):
      return cmd_name, cmd_task[2:]
    else:
      return 'invalid', []
  else:
    return 'invalid', []

def main():
  print('***********Todo CLI Application***********')
  current_task = ''
  while(1):
    # take the command as input from the user
    command = input('>>>>> ')
    command_name, command_args = parse(command)
    # print(command_name, command_args)
    if (command_name == 'exit'):
      if(len(command_args)):
        print('Please enter a valid command, use help command to display all!')
      else:
        break
    elif (command_name == 'help'):
      if(len(command_args)):
        print('Please enter a valid command, use help command to display all!')
      else:
        with open('help.txt', 'r') as help_file:
          print(help_file.read())
    elif (command_name == 'invalid'):
      print('Please enter a valid command, use help command to display all!')
    elif (command_name == 'use'):
      file_name = commands_dict1[command_name](command_args)
      if (file_name == -1):
        print('This is not a valid task name!')
        current_task = ''
      else:
        print('Successfuly chosen this task...')
        current_task = file_name
    elif (command.split()[0] == 'todo'):
      # todo type of command
      command_args.insert(0, current_task)
      commands_dict2[command_name](command_args)
    elif (command.split()[0] == 'task'):
      commands_dict1[command_name](command_args)

if __name__ == '__main__':
  main()