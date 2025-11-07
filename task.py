class Task:
  
  def __init__(self, title, id=None, done=False):
    self.id = id + 1
    # TODO PROBLEMA NO ID, AGORA QUE É NONE ELE NÃO PODE SOMAR MAS TAMBÉM SE NÃO FIZER ELE DUPLICA NO ARQUIVO DE ARMAZENAMENTO
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