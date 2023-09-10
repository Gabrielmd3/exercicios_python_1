import random

# Lista de letras não usadas
letras_nao_usadas = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

def carregar_palavras():
    """Carrega o arquivo txt com as palavras para o jogo da forca."""
    with open("lista_palavras.txt", "r", encoding="UTF-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    return palavras

def verificar_letras(tentativa_palavra):
    """Verifica as letras usadas pelo jogador e remove da lista de letras não usadas."""
    for letra in tentativa_palavra:
        for i in letras_nao_usadas:
            if i == letra:
                letras_nao_usadas.remove(letra)

def imprimir_letras_nao_usadas():
    """Exibe as letras que ainda não foram usadas pelo jogador."""
    print("Letras não usadas:")
    for letra in letras_nao_usadas:
        print(letra, end=" ")

def cor_letra(palavra, tentativa):
    """Verifica se a letra está correta e aplica cores para identificação na exibição."""
    cor = ""
    for i in range(len(palavra)):
        if tentativa[i] == palavra[i]:
            cor += "\033[92m" + tentativa[i] + "\033[0m"  # Letra correta na posição correta (Verde)
        elif tentativa[i] in palavra:
            cor += "\033[93m" + tentativa[i] + "\033[0m"  # Letra correta na posição errada (Amarelo)
        else:
            cor += tentativa[i]  # Letra errada (Sem cor)
    return cor

def escolher_palavra(tamanho, palavras):
    """Seleciona uma palavra aleatória do tamanho desejado."""
    palavras_filtradas = [palavra for palavra in palavras if len(palavra) == tamanho]
    return random.choice(palavras_filtradas)

def jogar():
    """Função principal para executar o jogo da forca."""
    palavras = carregar_palavras()
    
    while True:
        tamanho_palavra = input("Qual é o tamanho da palavra a ser adivinhada? (3 a 14 letras)\n")
        if tamanho_palavra.isdigit():
            tamanho_palavra = int(tamanho_palavra)
            if 3 <= tamanho_palavra <= 14:
                break
            else:
                print("A palavra deve ter entre 3 e 14 letras.")
        else:
            print("Número inválido! Digite um número!")

    palavra = escolher_palavra(tamanho_palavra, palavras)
    tentativas = 6

    print(f"A palavra secreta tem {tamanho_palavra} letras.\nBoa sorte!")

    while tentativas > 0:
        imprimir_letras_nao_usadas()
        tentativa = input(f"\nDigite a palavra com {tamanho_palavra} letras: ").lower()

        if len(tentativa) != tamanho_palavra or not tentativa.isalpha():
            print(f"Digite uma palavra válida, ela deve ter {tamanho_palavra} letras.")
            continue

        verificar_letras(tentativa)

        if tentativa == palavra:
            print(f"Você ganhou! A palavra é: {palavra}")
            break
        else:
            tentativas -= 1
            cor = cor_letra(palavra, tentativa)
            print(f"Palavra: {cor} - Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print(f"Você perdeu! A palavra era: {palavra}")

# Iniciar o jogo da forca
jogar()
