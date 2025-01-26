from pathlib import Path

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

    if not Path.exists(Path.cwd() / nome_arquivo):
        informacao("nenhuma tarefa encontrada", tamanho)
        return

    if len(ler_tarefas(nome_arquivo)) == 0:
        Path.unlink(Path.cwd() / nome_arquivo)
        informacao(mensagem="nenhuma tarefa encontrada", tamanho=tamanho)
        return

    menu_acoes(acoes, tamanho)
    tarefas: list[dict[str, str]] = ler_tarefas(nome_arquivo)

    while True:
        if len(tarefas) == 0:
            informacao("não há mais tarefas", tamanho)
            Path.unlink(Path.cwd() / nome_arquivo)
            break

        acao_escolhida: int = selecionar_acao(acoes, tamanho)

        if acao_escolhida != len(acoes):
            tarefas = executar(tarefas, acao_escolhida, nome_arquivo, tamanho)
        else:
            break

    if len(tarefas) > 0:
        criar_lista(nome_arquivo, tamanho)
        registrar_tarefas(tarefas, nome_arquivo)

    informacao("lista de tarefa atualizada", tamanho)


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
            tarefas = editar_titulo(tarefas, id, tamanho)
        case 3:
            tarefas = editar_descricao(tarefas, id, tamanho)
        case 4:
            tarefas = excluir_tarefa(tarefas, id)
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
    informacao("título atualizado", tamanho)
    return tarefas


def editar_descricao(
    tarefas: list[dict[str, str]], id: int, tamanho: int = 50
) -> list[dict[str, str]]:
    """Altera o título da tarefa com o id selecionado."""
    nova_descricao: str = entrada("nova descrição:", tamanho)
    tarefas[id - 1].update({"Descrição": nova_descricao})
    informacao("descrição atualizada", tamanho)
    return tarefas


def excluir_tarefa(tarefas: list[dict[str, str]], id: int) -> list[dict[str, str]]:
    """Exclui a tarefa com o id selecionado."""
    tarefas.pop(id - 1)
    informacao("tarefa excluída", tamanho=50)
    return tarefas
