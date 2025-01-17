from utilitarios import cabecalho


def imprimir(opcoes: list, tamanho=50) -> None:
    """Imprime o menu principal em formato personalizado."""
    cabecalho(texto="menu", tamanho=tamanho)
    print("-" * tamanho)
    for indice, opcao in enumerate(opcoes):
        print(f"[ {indice + 1} ]" + opcao.capitalize().center(tamanho - 10))
        print("-" * tamanho)


def main() -> None: ...


if __name__ == "__main__":
    main()
