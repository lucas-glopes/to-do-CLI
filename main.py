import menu
import adicionar_tarefas
from utilitarios import informacao


def executar(
    opcao_escolhida: int, nome_arquivo: str = "tarefa.csv", tamanho: int = 50
) -> None:
    """Executa as funções da opção escolhida pelo usuário."""
    match opcao_escolhida:
        case 1:
            adicionar_tarefas.adicionar(nome_arquivo, tamanho)
        case 2:
            ...
        case 3:
            ...
        case _:
            informacao("opção não implementada")


def main() -> None:
    OPCOES: list[str] = [
        "adicionar tarefas",
        "visualizar lista",
        "editar tarefas",
        "sair",
    ]
    TAMANHO: int = 50
    NOME_ARQUIVO: str = "tarefas.csv"

    menu.imprimir(opcoes=OPCOES, tamanho=TAMANHO)

    while True:
        opcao_escolhida: int = menu.selecionar_opcao(opcoes=OPCOES)
        if opcao_escolhida == len(OPCOES):
            informacao("programa encerrado")
            return
        executar(opcao_escolhida, nome_arquivo=NOME_ARQUIVO, tamanho=TAMANHO)


if __name__ == "__main__":
    main()
