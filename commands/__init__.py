import commands.tasks
import commands.todos

commands_dict1 = {
  'show': tasks.show_tasks,
  'use': tasks.use_task,
  'create': tasks.create_task,
  'remove': tasks.remove_task,
}
commands_dict2 = {
  'add': todos.add_item,
  'all': todos.show_items,
  'edit': todos.edit_item,
  'remove': todos.remove_item,
  'complete': todos.complete_item,
  'incomplete': todos.incomplete_item
}