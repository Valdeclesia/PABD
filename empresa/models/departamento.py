class Departamento:
    def __init__(self, id=None, nome=None, sigla=None):
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def to_dict(self):
        return {
            "nome": self.nome,
            "sigla": self.sigla
        }

    def __str__(self):
        return f"Departamento(id={self.id}, nome={self.nome}, sigla={self.sigla})"