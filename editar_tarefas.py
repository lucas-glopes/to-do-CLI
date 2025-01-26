from utilitarios import (
    cabecalho,
    criar_lista,
    entrada,
    entrada_id,
    erro,
    informacao,
    ler_tarefas,
    menu_acoes,
    registrar_tarefas,
    selecionar_acao,
)


def editar(
    acoes: list[str], nome_arquivo: str = "tarefas.csv", tamanho: int = 50
) -> None:
    """Imprime a lista de ações, recebe uma ação escolhida em loop e a executa."""
    cabecalho("editar tarefas", tamanho)
    menu_acoes(acoes, tamanho)
    tarefas: list[dict[str, str]] = ler_tarefas(nome_arquivo)

    while True:
        acao_escolhida: int = selecionar_acao(acoes, tamanho)
        if acao_escolhida != len(acoes):
            tarefas = executar(tarefas, acao_escolhida, nome_arquivo, tamanho)
        else:
            break

    criar_lista(nome_arquivo, tamanho)
    registrar_tarefas(tarefas, nome_arquivo)
    informacao("tarefas atualizadas", tamanho)


def executar(
    tarefas: list[dict[str, str]],
    acao_escolhida: int,
    nome_arquivo: str = "tarefas.csv",
    tamanho: int = 50,
) -> list[dict[str, str]]:
    """Executa as funções da ação escolhida pelo usuário."""
    id: int = entrada_id(nome_arquivo, tamanho)

    match acao_escolhida:
        case 1:
            tarefas = alterar_status(tarefas, id, tamanho)
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case _:
            informacao("ação não implementada", tamanho)

    return tarefas


def alterar_status(
    tarefas: list[dict[str, str]], id: int, tamanho: int = 50
) -> list[dict[str, str]]:
    """Altera o status da tarefa com o id selecionado."""
    if tarefas[id - 1]["Status"] == "pendente":
        tarefas[id - 1].update({"Status": "concluída"})
        informacao("tarefa marcada como -concluída-", tamanho)
    else:
        tarefas[id - 1].update({"Status": "pendente"})
        informacao("tarefa marcada como -pendente-", tamanho)

    return tarefas


def editar_titulo(
    tarefas: list[dict[str, str]], id: int, tamanho: int = 50
) -> list[dict[str, str]]:
    """Altera o título da tarefa com o id selecionado."""
    while True:
        novo_titulo: str = entrada("novo título:", tamanho)
        if len(novo_titulo) > 0:
            break
        erro("o título da tarefa é obrigatório!")

    tarefas[id - 1].update({"Título": novo_titulo})
    return tarefas


def editar_descricao(
    tarefas: list[dict[str, str]], id: int, tamanho: int = 50
) -> list[dict[str, str]]:
    """Altera o título da tarefa com o id selecionado."""
    nova_descricao: str = entrada("nova descrição:", tamanho)
    tarefas[id - 1].update({"Descrição": nova_descricao})
    return tarefas



def main() -> None: ...


if __name__ == "__main__":
    main()
