"""
main.py
Programa principal do sistema Orcamento de Aluguel - Imobiliaria R.M.

Aluna: Miriam Conrado Fernandes
Disciplina: Algorithmic Thinking & Introduction to Object-Oriented Programming
Instituicao: UniFECAF

Este arquivo controla o FLUXO da aplicacao:
entrada de dados -> criacao dos objetos -> calculo -> exibicao -> geracao do CSV
"""

from cliente import Cliente
from imovel import Apartamento, Casa, Estudio
from orcamento import Orcamento
from gerador_csv import GeradorCSV
import validacao


def exibir_cabecalho():
    print()
    print("=" * 52)
    print("     IMOBILIARIA R.M - SISTEMA DE ORCAMENTO")
    print("=" * 52)
    print()


def exibir_menu_imoveis():
    print("Tipos de imovel disponiveis:")
    print("  1 - Apartamento  (R$ 700,00 / 1 quarto)")
    print("  2 - Casa         (R$ 900,00 / 1 quarto)")
    print("  3 - Estudio      (R$ 1.200,00)")
    print()


def criar_imovel(opcao, cliente):
    """
    Cria o objeto do tipo escolhido pelo usuario.

    Cada tipo pede informacoes diferentes - por isso o if/elif.
    A funcao devolve um objeto Apartamento, Casa ou Estudio.
    """
    if opcao == 1:
        quartos = validacao.ler_inteiro("Quantos quartos (1 ou 2)? ", 1, 2)
        garagem = validacao.ler_sim_nao("Deseja vaga de garagem (+R$300,00)? [S/N] ")
        return Apartamento(quartos, garagem)

    elif opcao == 2:
        quartos = validacao.ler_inteiro("Quantos quartos (1 ou 2)? ", 1, 2)
        garagem = validacao.ler_sim_nao("Deseja vaga de garagem (+R$300,00)? [S/N] ")
        return Casa(quartos, garagem)

    else:
        print()
        print("Estacionamento do estudio: 2 vagas por R$250,00.")
        print("Cada vaga adicional alem das duas custa R$60,00.")
        vagas = validacao.ler_vagas_estudio("Quantas vagas deseja (0 ou 2 ou mais)? ")
        return Estudio(vagas)


def main():
    exibir_cabecalho()

    # ---------- 1. Dados do cliente ----------
    nome = validacao.ler_texto("Nome do cliente: ")
    possui_criancas = validacao.ler_sim_nao("O cliente possui criancas? [S/N] ")
    cliente = Cliente(nome, possui_criancas)

    # ---------- 2. Escolha do imovel ----------
    print()
    exibir_menu_imoveis()
    opcao = validacao.ler_inteiro("Escolha o tipo de imovel (1 a 3): ", 1, 3)

    print()
    imovel = criar_imovel(opcao, cliente)

    # ---------- 3. Contrato ----------
    print()
    print(f"Contrato imobiliario: R$ 2.000,00 (parcelavel em ate {Orcamento.MAXIMO_PARCELAS}x)")
    parcelas = validacao.ler_inteiro(
        "Em quantas vezes deseja parcelar o contrato (1 a 5)? ",
        1,
        Orcamento.MAXIMO_PARCELAS
    )

    # ---------- 4. Monta e exibe o orcamento ----------
    orcamento = Orcamento(cliente, imovel, parcelas)
    print()
    print(orcamento.gerar_resumo())

    # ---------- 5. Geracao opcional do CSV ----------
    print()
    gerar = validacao.ler_sim_nao("Deseja gerar o arquivo CSV com os 12 meses? [S/N] ")
    if gerar:
        caminho = GeradorCSV.gerar_csv(orcamento)
        print(f"\n  [OK] Arquivo gerado com sucesso em: {caminho}")
    else:
        print("\n  Arquivo CSV nao gerado.")

    print("\nObrigada por utilizar o sistema da Imobiliaria R.M!\n")


# Esta condicao garante que o programa so roda quando executamos main.py
# diretamente, e nao quando ele e importado por outro arquivo.
if __name__ == "__main__":
    main()
