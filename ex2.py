import time
import os

def criar_tabuleiro(dimensao):
    """Cria o tabuleiro do jogo da velha."""
    return [["-" for _ in range(dimensao)] for _ in range(dimensao)]

def imprimir_tabuleiro(dimensao):
    """Imprime o tabuleiro do jogo da velha."""
    for linha in tabuleiro:
        linha_formatada = " | ".join(linha)
        print(linha_formatada)
        print("--+--" * (dimensao - 1))

def verificar_vitoria(jogador, dimensao):
    """
    Verifica se o jogador ganhou o jogo.
    Verifica a vitória nas linhas, colunas e diagonais.
    """
    for linha in tabuleiro:  # Linhas
        if all(casa == jogador for casa in linha):
            return True

    for coluna in range(dimensao):  # Colunas
        if all(tabuleiro[linha][coluna] == jogador for linha in range(dimensao)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(dimensao)) or all(
        tabuleiro[i][dimensao - i - 1] == jogador for i in range(dimensao)
    ):  # Diagonais
        return True
    return False

def verificar_empate(dimensao, jogadas):
    """Verifica se houve empate."""
    if jogadas == dimensao * dimensao:
        return True
    else:
        return False

def jogar_jogo(dimensao):
    """Executa o jogo"""
    jogadas = 1
    jogador1 = "X"
    jogador2 = "O"
    while True:
        print(f"Vez do Jogador {1 if jogadas % 2 == 1 else 2}.")
        imprimir_tabuleiro(dimensao)
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if linha < 1 or linha > dimensao or coluna < 1 or coluna > dimensao:
                print("Fora de dimensão!")
                time.sleep(2)
                os.system("cls")
                continue

        except ValueError:
            print("Digite um número!")
            time.sleep(2)
            os.system("cls")
        else:

            if tabuleiro[linha - 1][coluna - 1] != "-":
                print("Esta casa já está ocupada.")
                time.sleep(2)
                continue
            else:
                if jogadas % 2 == 0:
                    tabuleiro[linha - 1][coluna - 1] = jogador2
                else:
                    tabuleiro[linha - 1][coluna - 1] = jogador1

            if verificar_vitoria(
                jogador1 if jogadas % 2 == 1 else jogador2, dimensao
            ):
                imprimir_tabuleiro(dimensao)
                print(f"Parabéns Jogador {jogadas % 2 + 1}, você ganhou!")
                time.sleep(2)
                break
            jogadas += 1
            if verificar_empate(dimensao, jogadas):
                imprimir_tabuleiro(dimensao)
                print("Empate!")
                time.sleep(2)
                break
            os.system("cls")


dimensao = int(input("Digite o tamanho da dimensão (deve ser 3 ou mais): "))
while dimensao < 3:
    dimensao = int(input("Tamanho muito pequeno.\nDigite o tamanho da dimensão (deve ser 3 ou mais): "))

tabuleiro = criar_tabuleiro(dimensao)
jogar_jogo(dimensao)
