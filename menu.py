from utilitarios import cabecalho, entrada, erro


def imprimir(opcoes: list[str], tamanho=50) -> None:
    """Imprime o menu principal em formato personalizado."""
    cabecalho(texto="menu", tamanho=tamanho)
    print("-" * tamanho)
    for indice, opcao in enumerate(opcoes):
        print(f"[ {indice + 1} ]" + opcao.capitalize().center(tamanho - 10))
        print("-" * tamanho)


def selecionar_opcao(opcoes: list[str], tamanho: int = 50) -> int:
    """Retorna o número da opção escolhida pelo usuário."""
    while True:
        opcao_escolhida: str = entrada("selecione uma opção:", tamanho).lower().strip()
        if opcao_valida(opcoes, opcao_escolhida):
            if opcao_escolhida in opcoes:
                return opcoes.index(opcao_escolhida) + 1
            else:
                return int(opcao_escolhida)
        else:
            erro("opção inválida!")


def opcao_valida(opcoes: list[str], opcao_escolhida: str) -> bool:
    """Retorna True caso a opção escolhida seja válida, caso contrário retorna False."""
    if opcao_escolhida in opcoes:
        return True
    elif opcao_escolhida.isnumeric():
        if 1 <= int(opcao_escolhida) <= len(opcoes):
            return True
        else:
            return False
    else:
        return False
