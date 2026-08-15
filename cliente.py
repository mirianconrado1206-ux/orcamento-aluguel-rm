"""
cliente.py
Classe que representa o cliente da imobiliaria R.M.

Conceitos da disciplina aplicados aqui:
- Classe e objeto (Unidade 3)
- Atributos definidos no construtor __init__
"""


class Cliente:
    """Representa o cliente que esta solicitando o orcamento."""

    def __init__(self, nome, possui_criancas):
        # self.nome e self.possui_criancas sao os ATRIBUTOS do objeto.
        # "self" e o proprio objeto: e por ele que guardamos os dados na instancia.
        self.nome = nome
        self.possui_criancas = possui_criancas

    def descricao_criancas(self):
        """Devolve um texto legivel para o resumo do orcamento."""
        if self.possui_criancas:
            return "Sim"
        return "Nao"

    def __str__(self):
        # __str__ define o que aparece quando usamos print(objeto).
        return f"Cliente: {self.nome}"
