"""
validacao.py
Funcoes responsaveis por receber e validar tudo que o usuario digita.

Conceitos da disciplina aplicados aqui:
- Limitando entrada de dados (Unidade 1)
- Laco while, if/elif/else
- Tratamento de erro com try/except e ValueError
- Funcoes com parametros e return (Unidade 2)
"""


def ler_texto(mensagem):
    """Le um texto e nao aceita resposta vazia."""
    valor = input(mensagem).strip()
    while valor == "":
        print("  [!] Esse campo nao pode ficar vazio. Tente novamente.")
        valor = input(mensagem).strip()
    return valor


def ler_inteiro(mensagem, minimo, maximo):
    """
    Le um numero inteiro dentro de uma faixa permitida.

    O try/except impede que o programa quebre se o usuario digitar letras:
    int("abc") gera um ValueError, que capturamos e tratamos.
    """
    while True:
        entrada = input(mensagem).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("  [!] Digite apenas numeros inteiros.")
            continue

        if numero < minimo or numero > maximo:
            print(f"  [!] Valor fora do permitido. Informe um numero de {minimo} a {maximo}.")
            continue

        return numero


def ler_sim_nao(mensagem):
    """Le uma resposta de sim ou nao e devolve True ou False."""
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("  [!] Responda apenas com S (sim) ou N (nao).")


def ler_vagas_estudio(mensagem):
    """
    Le a quantidade de vagas do estudio.

    Decisao de implementacao: o enunciado define o pacote minimo de 2 vagas
    por R$250,00 e nao informa preco para 1 vaga isolada. Por isso o sistema
    aceita 0 ou a partir de 2, sem inventar valor que nao existe no enunciado.
    """
    while True:
        vagas = ler_inteiro(mensagem, 0, 20)
        if vagas == 1:
            print("  [!] O estacionamento e vendido em pacote minimo de 2 vagas.")
            print("      Informe 0 (sem estacionamento) ou 2 ou mais vagas.")
            continue
        return vagas
