from .base_dao import BaseDAO
from ..models.funcionario import Funcionario

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        super().__init__("funcionario")

    def create_funcionario(self, funcionario: Funcionario):
        return self.create(funcionario.to_dict())

    def update_funcionario(self, id_value: int, funcionario: Funcionario):
        return self.update(id_value, funcionario.to_dict())