import menu


def executar(opcao_escolhida: int, nome_arquivo: str, tamanho: int):
    match opcao_escolhida:
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case _:
            ...


def main() -> None:
    OPCOES: list = ["adicionar tarefas", "visualizar lista", "editar tarefas", "sair"]
    TAMANHO: int = 50

    menu.imprimir(opcoes=OPCOES, tamanho=TAMANHO)
    opcao_escolhida: int = menu.selecionar_opcao(opcoes=OPCOES)


if __name__ == "__main__":
    main()
