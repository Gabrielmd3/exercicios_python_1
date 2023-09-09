import time
import os

def criar_tabuleiro(dimensao):
    """Cria o tabuleiro do jogo da velha."""
    return [["-" for _ in range(dimensao)] for _ in range(dimensao)]

def imprimir_tabuleiro(dif):
    """Imprime o tabuleiro do jogo da velha."""
    for i in tabuleiro:
        tab_final = " | ".join(i)
        print(tab_final)
        print("--+--"*(dif-1))


def ganhou(jogador, dimensao):
    """
    Verifica se o jogador ganhou o jogo.
    Verifica se ganhou o jogo em linha.
    Verifica se ganhou o jogo em diagonal.
    Verifica se ganhou o jogo em coluna.
    """
    
    for i in tabuleiro: #linha
        if all(x == jogador for x in i):
            return True
    
    for j in range(dimensao): #coluna
        if all(tabuleiro[l][j] == jogador for l in range(dimensao)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(dimensao) or tabuleiro[i][dimensao-i] == jogador for i in range(dimensao)): #diagonal
        return True
    return False

def empate(dimensao, jogadas):
    """Verifica se teve empate"""
    if jogadas == dimensao*dimensao:
        return True
    else:
        return False
                
def jogar_jogo(dimensao):
    """Executa o jogo"""
    jogadas = 1
    jogador1 = "X"
    jogador2 = "O"
    while True:
        print(f"Vez de Jogador {1 if jogadas%2 == 1 else 2}.")
        imprimir_tabuleiro(dimensao)
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if(linha < 1 or linha > dimensao or coluna < 1 or coluna > dimensao ):
                print("Fora de dimensão!")
                time.sleep(2)
                os.system('cls')
                continue

        except ValueError:
            print("Digite um número!")
            time.sleep(2)
            os.system('cls')
        else:
            
            if(tabuleiro[linha-1][coluna-1] != "-"):
                print("Está casa já está ocupada.")
                time.sleep(2)
                continue
            else:
                if(jogadas%2==0):
                    tabuleiro[linha-1][coluna-1] = jogador2
                else:
                    tabuleiro[linha-1][coluna-1] = jogador1
            
            if(ganhou(jogador1 if jogadas%2 == 1 else jogador2, dimensao)):
                imprimir_tabuleiro(dimensao)
                print(f"Parabéns Jogador {jogadas%2 + 1}, você ganhou!")
                time.sleep(2)
                break
            jogadas += 1
            if(empate(dimensao, jogadas)):
                imprimir_tabuleiro(dimensao)
                print("Empate!")
                time.sleep(2)
                break
            os.system('cls')

            
dimensao = int(input("Digite o tamanho da dimensão: "))
while dimensao < 3:
    dimensao = int(input("Tamanho muito pequeno.\nDigite o tamanho da dimensão: "))
    

tabuleiro = criar_tabuleiro(dimensao)
jogar_jogo(dimensao)

