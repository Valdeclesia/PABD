from .base_dao import BaseDAO
from ..models.departamento import Departamento

class DepartamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__("departamento")

    def create_departamento(self, departamento: Departamento):
        return self.create(departamento.to_dict())

    def update_departamento(self, id_value: int, departamento: Departamento):
        return self.update(id_value, departamento.to_dict())
