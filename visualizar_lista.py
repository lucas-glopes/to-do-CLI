from pathlib import Path

from utilitarios import (
    cabecalho,
    entrada,
    erro,
    informacao,
    ler_tarefas,
    menu_acoes,
    selecionar_acao,
)


def visualizar(
    acoes: list[str], nome_arquivo: str = "tarefas.csv", tamanho: int = 50
) -> None:
    """Imprime a lista de tarefas e a de ações, recebe uma ação escolhida em loop e a executa."""
    imprimir(nome_arquivo, tamanho)
    menu_acoes(acoes, tamanho)

    while True:
        acao_escolhida: int = selecionar_acao(acoes, tamanho)
        match acao_escolhida:
            case 1:
                id: int = entrada_id(nome_arquivo, tamanho)
                ver_detalhes(id, nome_arquivo, tamanho)
            case 2:
                return
            case _:
                informacao("ação não implementada", tamanho)


def imprimir(nome_arquivo: str = "tarefas.csv", tamanho: int = 50) -> None:
    """Imprime o cabeçalho e a lista de tarefas em formato personalizado."""
    cabecalho(texto="lista de tarefas", tamanho=tamanho)

    if not Path.exists(Path.cwd() / nome_arquivo):
        informacao(mensagem="nenhuma tarefa encontrada", tamanho=tamanho)
        return

    tarefas: list[dict[str, str]] = ler_tarefas(nome_arquivo)
    print("=" * tamanho)
    for indice, tarefa in enumerate(tarefas):
        titulo_tarefa, descricao_tarefa, status = list(tarefa.values())
        print(f"# {str(indice + 1):>2} | ", end="")

        if len(titulo_tarefa) <= tamanho - 21:
            print(f"{titulo_tarefa[: (tamanho - 21)]}", end="")
            print(f"[ {status.upper():<9} ]".rjust(tamanho - len(titulo_tarefa) - 7))
        else:
            print(f"{titulo_tarefa[: (tamanho - 24)]}...", end="")
            print(f"[ {status.upper():<9} ]".rjust(14))

        print("-" * tamanho)

        if len(descricao_tarefa) <= tamanho:
            print(descricao_tarefa)
        else:
            print(f"{descricao_tarefa[: tamanho - 3]}...")

        print("=" * tamanho)


def ver_detalhes(id: int, nome_arquivo: str = "tarefas.csv", tamanho: int = 50) -> None:
    """Imprime título, descrição e status completos de uma tarefa em formato personalizado."""
    tarefas: list[dict[str, str]] = ler_tarefas(nome_arquivo)
    titulo_tarefa, descricao_tarefa, status = list(tarefas[id - 1].values())

    print("=" * tamanho)
    print(f"# {str(id):>2} | ", end="")

    if len(titulo_tarefa) <= tamanho - 21:
        print(f"{titulo_tarefa[: (tamanho - 21)]}", end="")
        print(f"[ {status.upper():<9} ]".rjust(tamanho - len(titulo_tarefa) - 7))
    else:
        print(f"{titulo_tarefa[: (tamanho - 21)]}", end="")
        print(f"[ {status.upper():<9} ]".rjust(14))

        while len(titulo_tarefa) > tamanho - 21:
            titulo_tarefa = titulo_tarefa[(tamanho - 21) :]
            print(" " * 5 + "| " + titulo_tarefa[: tamanho - 21])

    print("-" * tamanho)

    if len(descricao_tarefa) <= tamanho:
        print(descricao_tarefa)
    else:
        print(f"{descricao_tarefa[:tamanho]}")

        while len(descricao_tarefa) > tamanho:
            descricao_tarefa = descricao_tarefa[tamanho:]
            print(descricao_tarefa[:tamanho])

    print("=" * tamanho)


def entrada_id(nome_arquivo: str = "tarefas.csv", tamanho: int = 50) -> int:
    """Recebe do usuário o ID de uma tarefa e o retorna."""
    tarefas: list[dict[str, str]] = ler_tarefas(nome_arquivo)

    while True:
        try:
            id: int = int(entrada("identificador (#) da tarefa:", tamanho))
        except ValueError:
            erro("entrada inválida!")
        else:
            if 1 <= id <= len(tarefas):
                return id
            else:
                erro("identificador não encontrado.")
