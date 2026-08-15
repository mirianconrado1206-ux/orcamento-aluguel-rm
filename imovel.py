"""
imovel.py
Classes que representam os tipos de imovel da imobiliaria R.M.

Conceitos da disciplina aplicados aqui:
- Abstracao: a classe Imovel define O QUE todo imovel faz, sem detalhar o COMO
- Heranca: Apartamento, Casa e Estudio herdam de Imovel
- Polimorfismo: cada tipo calcula desconto e adicionais do seu proprio jeito
- Encapsulamento: os dados ficam guardados dentro do objeto
"""


class Imovel:
    """
    Classe MAE (base) de todos os imoveis.

    Guarda o que e comum aos tres tipos:
    - um valor base de aluguel
    - uma lista de adicionais (descricao, valor)
    """

    # Constante compartilhada por casas e apartamentos.
    VALOR_GARAGEM = 300.00

    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base
        self.adicionais = []   # lista de tuplas: ("descricao", valor)

    def calcular_adicionais(self):
        """Soma todos os valores adicionais do imovel."""
        total = 0.0
        for descricao, valor in self.adicionais:
            total = total + valor
        return total

    def calcular_desconto(self, cliente, subtotal):
        """
        Regra padrao: nenhum desconto.
        As classes filhas que tiverem desconto sobrescrevem este metodo.
        Isso e POLIMORFISMO.
        """
        return 0.0

    def calcular_aluguel(self, cliente):
        """
        Calcula o aluguel mensal final.

        Ordem adotada (decisao de implementacao documentada no relatorio):
        1) valor base
        2) + adicionais (quarto extra, garagem, vagas)
        3) - desconto, aplicado sobre o subtotal ja com adicionais
        """
        subtotal = self.valor_base + self.calcular_adicionais()
        desconto = self.calcular_desconto(cliente, subtotal)
        return subtotal - desconto

    def __str__(self):
        return f"Imovel: {self.tipo}"


class Apartamento(Imovel):
    """Apartamento: R$700,00 (1 quarto). 2 quartos = +R$200,00. Garagem = +R$300,00."""

    VALOR_BASE = 700.00
    ACRESCIMO_SEGUNDO_QUARTO = 200.00
    PERCENTUAL_DESCONTO_SEM_CRIANCAS = 0.05   # 5%

    def __init__(self, quartos, tem_garagem):
        # super().__init__ chama o construtor da classe mae (heranca).
        super().__init__("Apartamento", Apartamento.VALOR_BASE)
        self.quartos = quartos
        self.tem_garagem = tem_garagem

        if quartos == 2:
            self.adicionais.append(("Acrescimo 2 quartos", Apartamento.ACRESCIMO_SEGUNDO_QUARTO))
        if tem_garagem:
            self.adicionais.append(("Vaga de garagem", Imovel.VALOR_GARAGEM))

    def calcular_desconto(self, cliente, subtotal):
        """
        SOBRESCRITA do metodo da classe mae.
        Desconto de 5% apenas para apartamentos de clientes SEM criancas.
        """
        if not cliente.possui_criancas:
            return subtotal * Apartamento.PERCENTUAL_DESCONTO_SEM_CRIANCAS
        return 0.0


class Casa(Imovel):
    """Casa: R$900,00 (1 quarto). 2 quartos = +R$250,00. Garagem = +R$300,00."""

    VALOR_BASE = 900.00
    ACRESCIMO_SEGUNDO_QUARTO = 250.00

    def __init__(self, quartos, tem_garagem):
        super().__init__("Casa", Casa.VALOR_BASE)
        self.quartos = quartos
        self.tem_garagem = tem_garagem

        if quartos == 2:
            self.adicionais.append(("Acrescimo 2 quartos", Casa.ACRESCIMO_SEGUNDO_QUARTO))
        if tem_garagem:
            self.adicionais.append(("Vaga de garagem", Imovel.VALOR_GARAGEM))

    # Casa NAO sobrescreve calcular_desconto: herda o comportamento padrao (sem desconto).


class Estudio(Imovel):
    """
    Estudio: R$1.200,00.
    Estacionamento: pacote de 2 vagas por R$250,00.
    Cada vaga adicional alem das duas custa R$60,00.
    """

    VALOR_BASE = 1200.00
    VALOR_PACOTE_DUAS_VAGAS = 250.00
    VALOR_VAGA_ADICIONAL = 60.00

    def __init__(self, vagas):
        super().__init__("Estudio", Estudio.VALOR_BASE)
        self.vagas = vagas

        if vagas >= 2:
            self.adicionais.append(("Pacote 2 vagas", Estudio.VALOR_PACOTE_DUAS_VAGAS))
            vagas_extras = vagas - 2
            if vagas_extras > 0:
                valor_extras = vagas_extras * Estudio.VALOR_VAGA_ADICIONAL
                self.adicionais.append((f"Vagas adicionais ({vagas_extras})", valor_extras))

    # Estudio tambem nao tem desconto: herda o padrao da classe mae.
