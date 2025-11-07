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
        json.dump(tasksFile, file, indent=4, ensure_ascii=False)

      print("Task added successfully")
    except:
      print('An exception occurred when trying to add a task.')

  def updateTask(self, title, done, id):
    print(self.tasks)
    task = self.tasks[int(id)]
    task.title = title
    task.done = done

    tasksFile = [task.toJSON() for task in self.tasks]
    with open('taskList.json', 'w', encoding='utf-8') as file:
      json.dump(tasksFile, file, indent=4, ensure_ascii=False)

    print("Task " + str(id) + " updated")

  def getTask(self, id):
    for task in self.tasks:
      if task.id == id:
        return task
      # TODO - ERRO QUE NÃO CONSEGUE LER O "OBJETO"

  def removeTask(self, id):
    task_remove = self.tasks[int(id)]

    try:
      self.tasks.remove(task_remove)
      
      tasksFile = [task.toJSON() for task in self.tasks]
      with open('taskList.json', 'w', encoding='utf-8') as file:
        json.dump(tasksFile, file, indent=4, ensure_ascii=False)

    except:
      print('An exception occurred when trying to remove a task.')

    print("Task removed")

  def showTasks(self):
    for task in self.tasks:
      print(task)




newTODOList = TODOList()

def start():
  while True:
    selected = input("""
          ====== O que deseja fazer: ======
          1 - Adicionar nova tarefa
          2 - Ver tarefas
          3 - Atualizar tarefa
          4 - Remover tarefa
          5 - Sair
          =================================
          """)
    if selected: break

  if selected == "1":
    task_title = input("Digite a task: ")
    newTODOList.addTask(task_title)
    start()
  elif selected == "2":
    newTODOList.showTasks()
    start()
  elif selected == "3":
    id = input("Digite o id da task que deseja atualizar: ")
    new_title = input("Digite o novo titulo: ")

    if not new_title:
      task = newTODOList.getTask(id)
      print(task)
      new_title = task.title

    updated_status = input("Concluida? [Sim-Nao]")
    
    if str.lower(updated_status) == 'sim':
      newTODOList.updateTask(new_title, True, id)
    else:
      newTODOList.updateTask(new_title, False, id)

    start()
  elif selected == "4":
    task_id = input("Digite o id da task que deseja remover: ")
    newTODOList.removeTask(task_id)
    start()

start()



# TODO - ADICIONAR ARMAZENAMENTO EXTERNO/PERSISTENTE
# TODO - INCREMENTAR PROJETO