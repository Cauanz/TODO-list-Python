import task
import json

class TODOList:
  def __init__(self):
    self.tasks = []
    with open('taskList.json', 'r', encoding='utf-8') as file:
      tasks_from = json.load(file)
      self.tasks = [task.Task(**data) for data in tasks_from]

  def addTask(self, title):
    newTask = task.Task(title)
    try:
      self.tasks.append(newTask)

      tasksFile = [task.toJSON() for task in self.tasks]
      with open('taskList.json', 'w', encoding='utf-8') as file:
        json.dump(tasksFile, file, indent=2, ensure_ascii=False)

      print("Task added successfully")
    except:
      print('An exception occurred when trying to add a task.')

  def updateTask(self, title, done, id):
    for task in self.tasks:
      if task.id == int(id):
        task.title = title
        task.done = done

    tasksFile = [task.toJSON() for task in self.tasks]
    with open('taskList.json', 'w', encoding='utf-8') as file:
      json.dump(tasksFile, file, indent=2, ensure_ascii=False)

    print("Task " + str(id) + " updated")

  def getTask(self, id):
    for task in self.tasks:
      if task.id == int(id):
        return task

  def removeTask(self, id):
    for i, ctask in enumerate(self.tasks):
      if ctask.id == int(id):
        task_remove = ctask 
        last_task_id = self.tasks[i-1].id
        task.Task.task_id = last_task_id

    try:
      self.tasks.remove(task_remove)
      
      tasksFile = [task.toJSON() for task in self.tasks]
      with open('taskList.json', 'w', encoding='utf-8') as file:
        json.dump(tasksFile, file, indent=2, ensure_ascii=False)

    except:
      print('An exception occurred when trying to remove a task.')

    print("Task removed")

  def showTasks(self):
    for task in self.tasks:
      print(task)
    print("\n", "All tasks: ", self.tasks)