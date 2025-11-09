import todolist

def start():
  newTODOList = todolist.TODOList()

  menu = """
  ====== O que deseja fazer: ======
  |  1 - Adicionar nova tarefa    |
  |  2 - Ver tarefas              |
  |  3 - Atualizar tarefa         |
  |  4 - Remover tarefa           |
  |  5 - Sair                     |
  =================================
  """

  while True:
    selected = input(menu)

    if selected == "1":
      task_title = input("Digite a task: ")
      newTODOList.addTask(task_title)

    elif selected == "2":
      newTODOList.showTasks()

    elif selected == "3":
      id = input("Digite o id da task que deseja atualizar: ")
      new_title = input("Digite o novo titulo: ")

      if not new_title:
        task = newTODOList.getTask(id)
        new_title = task.title

      updated_status = input("Concluida? [Sim-Nao]")
      
      if str.lower(updated_status) == 'sim':
        newTODOList.updateTask(new_title, True, id)
      else:
        newTODOList.updateTask(new_title, False, id)

    elif selected == "4":
      task_id = input("Digite o id da task que deseja remover: ")
      newTODOList.removeTask(task_id)
    
    elif selected == "5":
      print("Saindo...")
      break;

    else:
      print("Opção inválida")

start()