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
