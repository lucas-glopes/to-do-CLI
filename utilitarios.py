from sys import exit
import csv


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


def entrada(mensagem: str) -> str:
    """Recebe uma entrada do usuário."""
    try:
        return input(f">>> {mensagem.capitalize()} ")
    except KeyboardInterrupt:
        exit()


def erro(mensagem: str) -> None:
    """Imprime uma mensagem de erro em formato personalizado."""
    print(f"~ {mensagem.capitalize()}")


def informacao(mensagem: str, tamanho=50) -> None:
    """Imprime uma mensagem informativa em formato personalizado."""
    print()
    print(mensagem.upper().center(tamanho))
    print()


def ler_tarefas(nome_arquivo: str = "tarefas.csv") -> list[dict[str, str]]:
    """Lê o arquivo da lista e retorna as tarefas contidas nele."""
    tarefas: list[dict[str, str]] = []
    with open(nome_arquivo, "r") as arquivo_tarefas:
        leitor_csv: object = csv.DictReader(arquivo_tarefas)
        for tarefa in leitor_csv:
            tarefas.append(tarefa)
        arquivo_tarefas.close()
    tarefas.pop(0)
    return tarefas

