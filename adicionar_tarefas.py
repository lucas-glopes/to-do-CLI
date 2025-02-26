from pathlib import Path

from utilitarios import (
    cabecalho,
    criar_lista,
    entrada,
    erro,
    informacao,
    registrar_tarefas,
    titulo,
)


def adicionar(nome_arquivo: str = "tarefas.csv", tamanho: int = 50) -> None:
    """Recebe título e descrição das tarefas em loop e as registra na lista de tarefas."""
    if not Path.exists(Path.cwd() / nome_arquivo):
        criar_lista(nome_arquivo, tamanho, True)

    cabecalho(texto="adicionar tarefas", tamanho=tamanho)
    novas_tarefas: list[dict[str, str]] = []

    while True:
        titulo(texto="Nova tarefa", tamanho=tamanho)
        while True:
            titulo_tarefa: str = entrada("Título:", tamanho)
            if len(titulo_tarefa) > 0:
                break
            erro("o título da tarefa é obrigatório!")
        descricao_tarefa: str = entrada("Descrição:", tamanho)
        novas_tarefas.append(
            {
                "Título": titulo_tarefa,
                "Descrição": descricao_tarefa,
                "Status": "pendente",
            }
        )

        while True:
            continuar: str = (
                entrada("Adicionar mais tarefas? [s/n]", tamanho).lower().strip()
            )
            if resposta_valida(continuar):
                break
            erro("resposta inválida!")

        if continuar not in ["sim", "s"]:
            break

    registrar_tarefas(tarefas=novas_tarefas, nome_arquivo=nome_arquivo)
    informacao(mensagem="novas tarefas registradas", tamanho=tamanho)


def resposta_valida(resposta: str) -> bool:
    """Retorna True caso a resposta seja "sim" ou "não", caso contrário retorna False."""
    respostas_validas: list[str] = ["sim", "não", "nao", "s", "n"]
    return resposta in respostas_validas
