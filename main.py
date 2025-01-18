import menu


def main() -> None:
    OPCOES: list = ["adicionar tarefas", "visualizar lista", "editar tarefas", "sair"]
    TAMANHO: int = 50

    menu.imprimir(opcoes=OPCOES, tamanho=TAMANHO)
    opcao_escolhida: int = menu.selecionar_opcao(opcoes=OPCOES)


if __name__ == "__main__":
    main()
