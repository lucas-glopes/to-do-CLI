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
    return input(f">>> {mensagem.capitalize()} ")

