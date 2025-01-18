from sys import exit


def titulo(texto: str, tamanho: int = 50) -> None:
    """Imprime um título em formato personalizado."""
    print("-" * tamanho)
    print(texto.center(tamanho))
    print("-" * tamanho)


def cabecalho(texto: str, tamanho: int = 50) -> None:
    """Imprime um cabeçalho em formato personalizado."""
    print("=" * tamanho)
    print(texto.upper().center(tamanho))
    print("=" * tamanho)


def entrada(mensagem: str) -> str:
    """Recebe uma entrada do usuário."""
    try:
        return input(f">>> {mensagem.capitalize()} ")
    except KeyboardInterrupt:
        exit()


def erro(mensagem: str) -> None:
    """Imprime uma mensagem de erro em formato personalizado."""
    print(f"~ {mensagem.capitalize()}")


def informacao(mensagem: str, tamanho=50) -> None:
    """Imprime uma mensagem informativa em formato personalizado."""
    print()
    print(mensagem.upper().center(tamanho))
    print()
