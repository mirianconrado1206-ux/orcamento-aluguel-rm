"""
gerador_csv.py
Classe responsavel por gravar o orcamento em um arquivo .csv.

Conceitos da disciplina aplicados aqui:
- Manipulacao de arquivos com with open (Unidade 4)
- Modulo csv da biblioteca padrao do Python
"""

import csv
import os


class GeradorCSV:
    """Gera o arquivo CSV com a projecao de 12 meses do orcamento."""

    CABECALHO = ["Mes", "Aluguel", "Parcela_Contrato", "Total_Mes"]

    @staticmethod
    def gerar_csv(orcamento, caminho="orcamentos/orcamento_12_meses.csv"):
        """
        Grava o arquivo CSV e devolve o caminho onde ele foi salvo.

        Detalhes importantes:
        - newline="" evita linhas em branco entre os registros
        - encoding="utf-8" garante que acentos aparecam corretamente
        - delimiter=";" faz o Excel em portugues abrir o arquivo ja separado
        """
        # Garante que a pasta de destino existe antes de gravar.
        pasta = os.path.dirname(caminho)
        if pasta != "" and not os.path.exists(pasta):
            os.makedirs(pasta)

        linhas = orcamento.gerar_parcelas_12_meses()

        with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(GeradorCSV.CABECALHO)

            for linha in linhas:
                escritor.writerow([
                    linha["Mes"],
                    f"{linha['Aluguel']:.2f}",
                    f"{linha['Parcela_Contrato']:.2f}",
                    f"{linha['Total_Mes']:.2f}"
                ])

        return caminho
