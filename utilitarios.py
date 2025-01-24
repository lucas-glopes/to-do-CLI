import csv
from sys import exit


def titulo(texto: str, tamanho: int = 50) -> None:
    """Imprime um título em formato personalizado."""
    print("-" * tamanho)
    print(texto.center(tamanho))
    print("-" * tamanho)


def cabecalho(texto: str, tamanho: int = 50) -> None:
    """Imprime um cabeçalho em formato personalizado."""
    print("=" * tamanho)
    print(texto.upper().center(tamanho))
    print("=" * tamanho)


def entrada(mensagem: str, tamanho: int = 50) -> str:
    """Recebe uma entrada do usuário."""
    try:
        return input(f">>> {mensagem.capitalize()} ")
    except KeyboardInterrupt:
        print()
        informacao("programa encerrado", tamanho)
        exit()


def erro(mensagem: str) -> None:
    """Imprime uma mensagem de erro em formato personalizado."""
    print(f"~ {mensagem.capitalize()}")


def informacao(mensagem: str, tamanho: int = 50) -> None:
    """Imprime uma mensagem informativa em formato personalizado."""
    print()
    print(mensagem.upper().center(tamanho))
    print()


def ler_tarefas(nome_arquivo: str = "tarefas.csv") -> list[dict[str, str]]:
    """Lê o arquivo da lista e retorna as tarefas contidas nele."""
    tarefas: list[dict[str, str]] = []
    with open(nome_arquivo, "r") as arquivo_tarefas:
        leitor_csv: object = csv.DictReader(f=arquivo_tarefas, delimiter=";")
        for tarefa in leitor_csv:
            tarefas.append(tarefa)
        arquivo_tarefas.close()
    return tarefas


def registrar_tarefas(
    tarefas: list[dict[str, str]], nome_arquivo: str = "tarefas.csv"
) -> None:
    """Escreves a lista de novas tarefas no arquivo de lista."""
    with open(nome_arquivo, "a") as arquivo_tarefas:
        CAMPOS: list[str] = ["Título", "Descrição", "Status"]
        escritor_csv: object = csv.DictWriter(
            f=arquivo_tarefas, fieldnames=CAMPOS, delimiter=";"
        )
        escritor_csv.writerows(tarefas)
        arquivo_tarefas.close()


def menu_acoes(acoes: list, tamanho: int = 50) -> None:
    """Imprime o menu de ações em formato personalizado."""
    titulo(texto="Ações", tamanho=tamanho)
    print("-" * tamanho)

    for indice, acao in enumerate(acoes):
        print(f"( {indice + 1} )" + acao.capitalize().center(tamanho - 10))
    print("-" * tamanho)


def selecionar_acao(acoes: list[str], tamanho: int = 50) -> int:
    """Retorna o número da ação escolhida pelo usuário."""
    while True:
        acao_escolhida: str = entrada("selecione uma ação:", tamanho).lower().strip()
        if acao_valida(acoes, acao_escolhida):
            if acao_escolhida in acoes:
                return acoes.index(acao_escolhida) + 1
            else:
                return int(acao_escolhida)
        else:
            erro("opção inválida!")


def acao_valida(acoes: list[str], acao_escolhida: str) -> bool:
    """Retorna True caso a ação seja válida, caso contrário retorna False."""
    if acao_escolhida in acoes:
        return True
    elif acao_escolhida.isnumeric():
        if 1 <= int(acao_escolhida) <= len(acoes):
            return True
        else:
            return False
    else:
        return False
