import time


tabuleiro = [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]
]

def imprimir_tabuleiro():
    """Imprime o tabuleiro do jogo da velha."""
    for i in tabuleiro:
        tab_final = " | ".join(i)
        print(tab_final)
        print("--+---+---+---")


def ganhou(jogador):
    """
    Verifica se o jogador ganhou o jogo.
    Verifica se ganhou o jogo em linha.
    Verifica se ganhou o jogo em diagonal.
    Verifica se ganhou o jogo em coluna.
    """
    #linha
    for i in tabuleiro:
        if all(x == jogador for x in i):
            return True
    #coluna
    for j in range(4):
        if all(tabuleiro[l][j] == jogador for l in range(4)):
            return True
    #diagonal
    if all(tabuleiro[i][i] == jogador for i in range(4) or tabuleiro[i][4-i] == jogador for i in range(4)):
        return True
    return False

def empate(jogadas):
    """Verifica se teve empate"""
    if jogadas == 4*4:
        return True
    else:
        return False
                
def jogar_jogo():
    """Executa o jogo"""
    jogadas = 1
    jogador1 = "X"
    jogador2 = "O"
    while True:
        print(f"Vez de Jogador {jogadas%2 + 1}.")
        imprimir_tabuleiro()
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if(linha < 1 or linha > 4 or coluna < 1 or coluna > 4 ):
                print("Fora de dimensão!")
                time.sleep(2)
                continue
        except ValueError:
            print("Digite um número!")
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
            
            if(ganhou(jogador1 if jogadas%2 == 1 else jogador2)):
                imprimir_tabuleiro()
                print(f"Parabéns Jogador {jogadas%2 + 1}, você ganhou!")
                time.sleep(2)
                break
            jogadas += 1
            if(empate(jogadas)):
                imprimir_tabuleiro()
                print("Empate!")
                time.sleep(2)
                break
            
jogar_jogo()


