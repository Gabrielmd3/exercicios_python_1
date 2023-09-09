import random

"""A lista letras_nao_usadas, basicamente vai retirar as letras conforme a pessoa escreve as palavras, assim mostrando somente as letras não usadas pelo jogador"""
letras_nao_usadas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def carregar_palavras():
    """Carrega o arquivo txt com as palavras, isso foi passado pelo proprio professor"""
    with open("lista_palavras.txt", "r", encoding="UTF-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    return palavras



def verificar_letras(tentativa_palavra):
    """A função verifica a palavra tentada pelo jogado"""
    for l in tentativa_palavra:
        for i in letras_nao_usadas:
            if i == l:
                letras_nao_usadas.remove(l)

def imprimir_letras_nao_usadas():
    """A função imprime as letras que ainda não foram usadas pelo jogador"""
    print("Letras não usadas:")
    for i in letras_nao_usadas:
        print(i, end=" ")
        


def cor_letra(palavra, tentativa):
    """Verifica se a letra esta correta, em uma posição certa ou errada, deixando uma cor para identificar"""
    cor = ""
    for i in range(len(palavra)):
        if tentativa[i] == palavra[i]:
            cor += "\033[92m" + tentativa[i] + "\033[0m"  # Posição certa: Verde
        elif tentativa[i] in palavra:
            cor += "\033[93m" + tentativa[i] + "\033[0m"  # Posição errada: Amarelo
        else:
            cor += tentativa[i]  # Letra errada: Não muda a cor
    return cor


def escolher_palavra(tamanho, palavras):
    """A função pega a lista de palavras e depois coloca em outra lista as palavars que tem o tamanho requerido pelo usuario, depois sorteia uma dessas palavras"""
    palavras_filtradas = [palavra for palavra in palavras if len(palavra) == tamanho]
    return random.choice(palavras_filtradas)



def jogar():
    """Principal função, ela inicia o jogo e chama as demais funções"""
    palavras = carregar_palavras()
    
     
    while True: # Pergunta o tamanho da palavra e verifica se ela é um número e se está no intervalo correto
        tamanho_palavra = input("Qual é  tamanho da palavra que seja advinhar?(3 à 14 letras)\n")
        if tamanho_palavra.isdigit():
            tamanho_palavra = int(tamanho_palavra)
            if 3 <= tamanho_palavra <= 14:
                break
            else:
                print("A palavra deve ter entre 3 e 14 palavras.")
        else:
            print("Número inválido! Digite um número!")

    
    palavra = escolher_palavra(tamanho_palavra, palavras) # Pega a palavra conforme o tamanho que o jogador escolheu
    tentativas = 6

    print(f"A palavra secreta tem {tamanho_palavra} letras.\nBoa sorte!")
    
    while tentativas > 0:
        
        imprimir_letras_nao_usadas() 
        tentativa = input(f"\nDigite a palavra com {tamanho_palavra} letras: ").lower()
        
        if len(tentativa) != tamanho_palavra or not tentativa.isalpha(): # Verifica se a palavra é uma palavra e se ela tem o tamanho nescessário
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
        print(f"Você perdeu! A palavra é: {palavra}")



"""Chama a função principal e inicia o jogo"""
jogar()
