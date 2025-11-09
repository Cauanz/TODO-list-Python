class Task:
  task_id = 0
  def __init__(self, title, id=None, done=False):
    if id is not None:
      self.id = id
      Task.task_id = id
    else:
      Task.task_id += 1
      self.id = Task.task_id
    self.title = title
    self.done = done

  def toJSON(self):
    return {
      'id': self.id, 
      'title': self.title, 
      'done': self.done
      }

  def __repr__(self):
    # representação não ambígua para debugging
    return f"Task(id={self.id!r}, title={self.title!r}, done={self.done!r})"

  def __str__(self):
    # representação legível para usuários
    status = '✓' if self.done else '✗'
    return f"{self.id} - {self.title} [{status}]"