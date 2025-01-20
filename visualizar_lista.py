from utilitarios import cabecalho, informacao, ler_tarefas
from pathlib import Path


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
            print(f"{titulo_tarefa[:(tamanho - 21)]}", end="")
            print(f"[ {status.upper():<9} ]".rjust(tamanho - len(titulo_tarefa) - 7))
        else:
            print(f"{titulo_tarefa[:(tamanho - 24)]}...", end="")
            print(f"[ {status.upper():<9} ]".rjust(14))

        print("-" * tamanho)

        if len(descricao_tarefa) <= tamanho:
            print(descricao_tarefa)
        else:
            print(f"{descricao_tarefa[:tamanho - 3]}...")

        print("=" * tamanho)


def main() -> None: ...


if __name__ == "__main__":
    main()
