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
        print()
        informacao("programa encerrado")
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
        leitor_csv: object = csv.DictReader(f=arquivo_tarefas, delimiter=";")
        for tarefa in leitor_csv:
            tarefas.append(tarefa)
        arquivo_tarefas.close()
    tarefas.pop(0)
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


def resposta_valida(resposta: str) -> bool:
    """Retorna True caso a resposta seja "sim" ou "não", caso contrário retorna False."""
    respostas_validas: list[str] = ["sim", "não", "nao", "s", "n"]
    return resposta in respostas_validas


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
