# Orçamento de Aluguel — Imobiliária R.M

Aplicação em Python para geração automatizada de orçamentos de locação de imóveis, desenvolvida como trabalho da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming** da UniFECAF.

---

## Sobre o projeto

A imobiliária R.M trabalha com locação de apartamentos, casas e estúdios. Cada tipo tem valor base próprio e regras específicas de acréscimo, o que torna o cálculo manual lento e sujeito a erro.

Esta aplicação automatiza esse cálculo: coleta os dados do cliente e do imóvel, aplica todas as regras comerciais da empresa, apresenta o orçamento formatado e gera um arquivo CSV com a projeção de 12 meses.

## Objetivo

Calcular o valor do aluguel mensal conforme as regras da imobiliária, apresentar o contrato imobiliário com as opções de parcelamento e permitir a exportação do orçamento em formato CSV.

## Regras de negócio

| Regra | Valor / condição |
|---|---|
| Apartamento — valor base | R$ 700,00 (1 quarto) |
| Apartamento — 2 quartos | + R$ 200,00 |
| Casa — valor base | R$ 900,00 (1 quarto) |
| Casa — 2 quartos | + R$ 250,00 |
| Garagem (casa e apartamento) | + R$ 300,00 |
| Estúdio — valor base | R$ 1.200,00 |
| Estúdio — estacionamento | R$ 250,00 pelo pacote de 2 vagas |
| Estúdio — vaga adicional | R$ 60,00 por vaga além das duas |
| Desconto | 5% sobre o aluguel de apartamento para cliente sem crianças |
| Contrato imobiliário | R$ 2.000,00, parcelável em até 5 vezes |

### Decisões de implementação

O enunciado admitia mais de uma leitura em alguns pontos. As interpretações adotadas foram:

- **Base do desconto de 5%:** aplicado sobre o subtotal, ou seja, após os acréscimos de quarto e garagem, pois a garagem compõe a mensalidade.
- **Desconto restrito a apartamentos:** casa e estúdio não recebem o benefício, conforme o texto do enunciado.
- **Estúdio não possui faixa de quartos:** o enunciado define valor único.
- **Estacionamento de 1 vaga:** não ofertado. O enunciado prevê o pacote de duas vagas e o valor da vaga adicional, mas não o preço de uma vaga isolada — o sistema informa a regra ao usuário em vez de arbitrar um valor inexistente.
- **Composição das 12 linhas do CSV:** o contrato admite no máximo 5 parcelas, portanto as 12 linhas correspondem a 12 meses de locação. O aluguel aparece nos 12 meses; a parcela do contrato, apenas nos meses do parcelamento escolhido.

## Funcionalidades

- Cadastro do cliente com identificação de existência de crianças
- Menu de seleção entre apartamento, casa e estúdio
- Cálculo automático de acréscimos, vagas e desconto
- Parcelamento do contrato de 1 a 5 vezes
- Resumo do orçamento formatado em reais
- Exportação opcional em CSV com projeção de 12 meses
- Validação completa das entradas do usuário

## Tecnologias utilizadas

- **Python 3** — linguagem de desenvolvimento
- **Módulo `csv`** — geração do arquivo (biblioteca padrão)
- **Módulo `os`** — verificação de diretórios (biblioteca padrão)

> O projeto **não possui dependências externas**. Utiliza apenas a biblioteca padrão do Python.

## Estrutura do projeto

```
orcamento_aluguel_rm/
├── main.py                  # fluxo principal da aplicação
├── cliente.py               # classe Cliente
├── imovel.py                # classe Imovel + Apartamento, Casa, Estudio
├── orcamento.py             # classe Orcamento e formatação monetária
├── gerador_csv.py           # classe GeradorCSV
├── validacao.py             # funções de validação de entrada
├── README.md
├── orcamentos/
│   └── orcamento_12_meses.csv
├── documentacao/
│   ├── fluxograma_orcamento.png
│   └── relatorio_teorico.pdf
└── testes/
    └── cenarios_testados.txt
```

## Como executar

Requer Python 3 instalado. Na pasta raiz do projeto:

```
python main.py
```

## Geração do CSV

Ao final do orçamento o sistema pergunta se o usuário deseja gerar o arquivo. Em caso afirmativo, é criado `orcamentos/orcamento_12_meses.csv` com as colunas:

| Mes | Aluguel | Parcela_Contrato | Total_Mes |
|---|---|---|---|
| 1 | 1140.00 | 400.00 | 1540.00 |
| ... | ... | ... | ... |
| 6 | 1140.00 | 0.00 | 1140.00 |

O arquivo usa `delimiter=";"` e `encoding="utf-8"`, abrindo diretamente no Excel em português.

## Orientação a Objetos aplicada

| Pilar | Onde aparece |
|---|---|
| **Abstração** | `Imovel` define o que todo imóvel faz, sem detalhar o cálculo de cada tipo |
| **Herança** | `Apartamento`, `Casa` e `Estudio` herdam de `Imovel` via `super().__init__()` |
| **Polimorfismo** | `calcular_desconto()` é sobrescrito em `Apartamento`; casa e estúdio mantêm o comportamento herdado |
| **Encapsulamento** | Os dados de cada imóvel ficam contidos no próprio objeto e são acessados por seus métodos |

## Cenários testados

15 cenários cobrindo os três tipos de imóvel, o desconto, os adicionais, todas as opções de parcelamento e a geração do arquivo. Todos com resultado conforme o esperado.

## Autor

**Miriam Conrado Fernandes**

## Disciplina

Algorithmic Thinking & Introduction to Object-Oriented Programming

## Instituição

UniFECAF — Centro Universitário Capital Federal  
Curso de Análise e Desenvolvimento de Sistemas — 2026
