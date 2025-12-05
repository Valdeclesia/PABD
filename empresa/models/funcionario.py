class Funcionario:
    def __init__(self, id: int | None, nome: str, salario: float, id_departamento: int):
        self.id = id
        self.nome = nome
        self.salario = salario
        self.id_departamento = id_departamento

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "salario": self.salario,
            "id_departamento": self.id_departamento
        }