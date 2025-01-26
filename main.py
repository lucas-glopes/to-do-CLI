import adicionar_tarefas
import editar_tarefas
import menu
import visualizar_lista
from utilitarios import informacao


def executar(
    opcao_escolhida: int, nome_arquivo: str = "tarefa.csv", tamanho: int = 50
) -> None:
    """Executa as funções da opção escolhida pelo usuário."""
    match opcao_escolhida:
        case 1:
            adicionar_tarefas.adicionar(nome_arquivo, tamanho)
        case 2:
            ACOES: list[str] = ["ver detalhes", "voltar ao menu"]
            visualizar_lista.visualizar(ACOES, nome_arquivo, tamanho)
        case 3:
            ACOES = [
                "alterar status",
                "editar título",
                "editar descrição",
                "excluir tarefa",
                "voltar ao menu",
            ]
            editar_tarefas.editar(ACOES, nome_arquivo, tamanho)
        case _:
            informacao("opção não implementada", tamanho)


def main() -> None:
    OPCOES: list[str] = [
        "adicionar tarefas",
        "visualizar lista",
        "editar tarefas",
        "sair",
    ]
    TAMANHO: int = 50
    NOME_ARQUIVO: str = "tarefas.csv"

    while True:
        menu.imprimir(opcoes=OPCOES, tamanho=TAMANHO)
        opcao_escolhida: int = menu.selecionar_opcao(opcoes=OPCOES, tamanho=TAMANHO)
        if opcao_escolhida == len(OPCOES):
            informacao("programa encerrado", tamanho=TAMANHO)
            return
        executar(opcao_escolhida, nome_arquivo=NOME_ARQUIVO, tamanho=TAMANHO)


if __name__ == "__main__":
    main()
