from funcionario.funcionario import Funcionario

class ControleDeBonificacoes:

  __slots__ = ['_total']

  def __init__(self, total = 0):
    self._total = total

  def registra(self, obj):
    if(isinstance(obj, Funcionario)):
      self._total += obj.get_bonificacao()
    else:
      print(f'Instância de {obj.__class__.__name__} não implementa o método get_bonificacao()')

  @property
  def total(self):
    return self._total