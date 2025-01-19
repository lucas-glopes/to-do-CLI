def main() -> None: ...
from pathlib import Path

from utilitarios import (
    cabecalho,
    titulo,
    entrada,
    erro,
    informacao,
    registrar_tarefas,
    resposta_valida,
)

import csv


def adicionar(nome_arquivo: str = "tarefas.csv", tamanho: int = 50) -> None:
    """Recebe título e descrição das tarefas em loop e as registra na lista de tarefas."""
    if not Path.exists(Path.cwd() / nome_arquivo):
        criar_lista(nome_arquivo, tamanho)

    cabecalho(texto="adicionar tarefas", tamanho=tamanho)
    novas_tarefas: list[dict[str, str]] = []

    while True:
        titulo(texto="Nova tarefa", tamanho=tamanho)
        while True:
            titulo_tarefa: str = entrada("Título:")
            if len(titulo_tarefa) > 0:
                break
            erro("o título da tarefa é obrigatório!")
        descricao_tarefa: str = entrada("Descrição:")
        novas_tarefas.append(
            {
                "Título": titulo_tarefa,
                "Descrição": descricao_tarefa,
                "Status": "pendente",
            }
        )

        while True:
            continuar: str = entrada("Adicionar mais tarefas? [s/n]").lower().strip()
            if resposta_valida(continuar):
                break
            erro("resposta inválida!")

        if not continuar in ["sim", "s"]:
            break

    registrar_tarefas(tarefas=novas_tarefas, nome_arquivo=nome_arquivo)
    informacao(mensagem="novas tarefas registradas", tamanho=tamanho)


def criar_lista(nome_arquivo: str = "tarefas.csv", tamanho=50) -> None:
    """Cria/sobrescreve o arquivo de lista com o nome fornecido."""
    with open(nome_arquivo, "w") as arquivo_tarefas:
        CAMPOS: list[str] = ["Título", "Descrição", "Status"]
        escritor_csv: object = csv.DictWriter(f=arquivo_tarefas, fieldnames=CAMPOS)
        escritor_csv.writeheader()
        arquivo_tarefas.close()

    informacao(mensagem=f'arquivo "{nome_arquivo}" criado', tamanho=tamanho)


def main() -> None:
if __name__ == "__main__":
    main()
