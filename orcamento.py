"""
orcamento.py
Classe que junta cliente + imovel + contrato e produz o orcamento final.

Conceitos da disciplina aplicados aqui:
- Composicao: um Orcamento CONTEM um Cliente e um Imovel
- Listas e dicionarios (Unidade 2)
- Laco for com range (Unidade 1)
"""


def formatar_moeda(valor):
    """
    Formata um numero no padrao brasileiro: 1140.0 -> R$ 1.140,00

    Como funciona:
    - f"{valor:,.2f}" gera o padrao americano (1,140.00)
    - depois trocamos os separadores para o padrao brasileiro
    """
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


class Orcamento:
    """Monta o orcamento completo: aluguel mensal + contrato parcelado."""

    VALOR_CONTRATO = 2000.00
    MAXIMO_PARCELAS = 5
    MESES_PROJECAO = 12

    def __init__(self, cliente, imovel, quantidade_parcelas):
        self.cliente = cliente
        self.imovel = imovel
        self.quantidade_parcelas = quantidade_parcelas
        # O calculo do aluguel e delegado ao objeto imovel (polimorfismo em acao).
        self.valor_aluguel = imovel.calcular_aluguel(cliente)

    def calcular_valor_parcela_contrato(self):
        """Divide o valor do contrato pela quantidade de parcelas escolhida."""
        return Orcamento.VALOR_CONTRATO / self.quantidade_parcelas

    def gerar_parcelas_12_meses(self):
        """
        Monta a projecao de 12 meses.

        Decisao de implementacao (documentada no relatorio e no README):
        o enunciado nao detalha a composicao das 12 linhas, entao adotamos
        12 meses de aluguel, com a parcela do contrato aparecendo apenas
        nos meses correspondentes ao parcelamento escolhido.
        """
        valor_parcela = self.calcular_valor_parcela_contrato()
        linhas = []

        for mes in range(1, Orcamento.MESES_PROJECAO + 1):
            if mes <= self.quantidade_parcelas:
                parcela_contrato = valor_parcela
            else:
                parcela_contrato = 0.0

            total_mes = self.valor_aluguel + parcela_contrato

            linhas.append({
                "Mes": mes,
                "Aluguel": round(self.valor_aluguel, 2),
                "Parcela_Contrato": round(parcela_contrato, 2),
                "Total_Mes": round(total_mes, 2)
            })

        return linhas

    LARGURA_ROTULO = 22

    def _linha(self, rotulo, valor):
        """Monta uma linha do resumo com os rotulos sempre alinhados."""
        return f"{rotulo:.<{Orcamento.LARGURA_ROTULO}}: {valor}"

    def gerar_resumo(self):
        """Monta o texto do orcamento que sera exibido na tela."""
        linhas = []
        linhas.append("=" * 52)
        linhas.append("       ORCAMENTO DE ALUGUEL - IMOBILIARIA R.M")
        linhas.append("=" * 52)
        linhas.append(self._linha("Cliente", self.cliente.nome))
        linhas.append(self._linha("Tipo de imovel", self.imovel.tipo))

        # Quartos so fazem sentido para apartamento e casa.
        if hasattr(self.imovel, "quartos"):
            linhas.append(self._linha("Quartos", self.imovel.quartos))

        if hasattr(self.imovel, "tem_garagem"):
            if self.imovel.tem_garagem:
                linhas.append(self._linha("Garagem", "Sim"))
            else:
                linhas.append(self._linha("Garagem", "Nao"))

        if hasattr(self.imovel, "vagas"):
            linhas.append(self._linha("Vagas estacionamento", self.imovel.vagas))

        # Criancas so influenciam no caso do apartamento.
        if self.imovel.tipo == "Apartamento":
            linhas.append(self._linha("Possui criancas", self.cliente.descricao_criancas()))

        linhas.append("-" * 52)
        linhas.append(self._linha("Valor base", formatar_moeda(self.imovel.valor_base)))

        if len(self.imovel.adicionais) == 0:
            linhas.append(self._linha("Adicionais", "nenhum"))
        else:
            for descricao, valor in self.imovel.adicionais:
                linhas.append(self._linha("+ " + descricao, formatar_moeda(valor)))

        subtotal = self.imovel.valor_base + self.imovel.calcular_adicionais()
        desconto = self.imovel.calcular_desconto(self.cliente, subtotal)
        if desconto > 0:
            linhas.append(self._linha("- Desconto 5%", formatar_moeda(desconto)))

        linhas.append("-" * 52)
        linhas.append(self._linha("ALUGUEL MENSAL", formatar_moeda(self.valor_aluguel)))
        linhas.append("-" * 52)
        linhas.append(self._linha("Contrato imobiliario", formatar_moeda(Orcamento.VALOR_CONTRATO)))
        linhas.append(self._linha("Parcelas do contrato", f"{self.quantidade_parcelas}x"))
        linhas.append(self._linha("Valor de cada parcela",
                                  formatar_moeda(self.calcular_valor_parcela_contrato())))
        linhas.append("=" * 52)

        return "\n".join(linhas)
