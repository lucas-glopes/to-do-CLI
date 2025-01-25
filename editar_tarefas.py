from utilitarios import cabecalho, informacao, menu_acoes, selecionar_acao
from utilitarios import (
    cabecalho,
    entrada_id,
    informacao,
    menu_acoes,
    selecionar_acao,


def editar(
    acoes: list[str], nome_arquivo: str = "tarefas.csv", tamanho: int = 50
) -> None:
    cabecalho("editar tarefas")
    menu_acoes(acoes, tamanho)

    while True:
        acao_escolhida: int = selecionar_acao(acoes, tamanho)
        if acao_escolhida != len(acoes):
            executar(acao_escolhida, tamanho)
        else:
            return

def executar(
    tarefas: list[dict[str, str]],
    acao_escolhida: int,
    nome_arquivo: str = "tarefas.csv",
    tamanho: int = 50,
) -> list[dict[str, str]]:
    id: int = entrada_id(nome_arquivo, tamanho)

    match acao_escolhida:
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case _:
            informacao("ação não implementada", tamanho)

    return tarefas


def alterar_status(
    tarefas: list[dict[str, str]], id: int, tamanho: int = 50
) -> list[dict[str, str]]:
    if tarefas[id - 1]["Status"] == "pendente":
        tarefas[id - 1].update({"Status": "concluída"})
        informacao("tarefa marcada como -concluída-", tamanho)
    else:
        tarefas[id - 1].update({"Status": "pendente"})
        informacao("tarefa marcada como -pendente-", tamanho)

    return tarefas



def main() -> None: ...


if __name__ == "__main__":
    main()
