import time

tabuleiro = [
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"]
]

def imprimir_tabuleiro():
    """Função para exibir o estado atual do tabuleiro do jogo da velha."""
    for linha in tabuleiro:
        linha_formatada = " | ".join(linha)
        print(linha_formatada)
        print("--+---+---+---")

def verificar_vitoria(jogador):
    """
    Função para verificar se o jogador atual venceu o jogo.
    Verifica se o jogador ganhou nas linhas, colunas e diagonais.
    """
    # Verificar linhas
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    # Verificar colunas
    for coluna in range(4):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(4)):
            return True
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True
    return False

def verificar_empate(jogadas):
    """Função para verificar se houve um empate no jogo."""
    if jogadas == 4 * 4:
        return True
    else:
        return False
                
def jogar_jogo():
    """Função principal para executar o jogo da velha."""
    jogadas = 1
    jogador1 = "X"
    jogador2 = "O"
    while True:
        print(f"Vez do Jogador {jogadas % 2 + 1}.")
        imprimir_tabuleiro()
        try:
            linha = int(input("Digite a linha (1-4): "))
            coluna = int(input("Digite a coluna (1-4): "))
            if linha < 1 or linha > 4 or coluna < 1 or coluna > 4:
                print("Posição fora de dimensão!")
                time.sleep(2)
                continue
        except ValueError:
            print("Digite um número válido!")
        else:
            if tabuleiro[linha - 1][coluna - 1] != "-":
                print("Esta posição já está ocupada.")
                time.sleep(2)
                continue
            else:
                if jogadas % 2 == 0:
                    tabuleiro[linha - 1][coluna - 1] = jogador2
                else:
                    tabuleiro[linha - 1][coluna - 1] = jogador1
            
            if verificar_vitoria(jogador1 if jogadas % 2 == 1 else jogador2):
                imprimir_tabuleiro()
                print(f"Parabéns Jogador {jogadas % 2 + 1}, você ganhou!")
                time.sleep(2)
                break
            jogadas += 1
            if verificar_empate(jogadas):
                imprimir_tabuleiro()
                print("O jogo terminou em empate!")
                time.sleep(2)
                break

# Iniciar o jogo
jogar_jogo()
