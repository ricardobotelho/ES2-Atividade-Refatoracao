from random import choice
import time

def titulo(mensagem, simbolo="-="):
    print()
    print(simbolo*15)
    print(mensagem)
    print(simbolo*15)

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor():
    print("Que pena! você perdeu!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

while True:
    time.sleep(1)
    titulo("JOGO DA FORCA", "-=")
    time.sleep(1)
    print("[1] JOGAR")
    print("[2] SAIR")
    opcao = int(input("OPÇÃO: "))
    if opcao == 1:
        time.sleep(1)
        print()
        print("QUAL ASSUNTO VOCÊ ESCOLHE ?")
        print("-="*15)
        print()
        print("AVISO: VOCÊ TEM 7 CHANCES PARA ACERTAR A PALAVRA")
        print()
        print("[1] ANIMAL")
        print("[2] VEGETAL")
        print("[3] CIDADE")
        print("[4] PROGRAMAÇÃO")
        print("[5] VOLTAR")
        print()
        print("PRIMEIRA DICA: ESPAÇO IGUAL A HÍFEN")
        print("SEGUNDA DICA: NÃO USAR ACENTO NA LETRA")
        print()
        time.sleep(1)
        tipo = int(input("OPÇÃO: "))
        if tipo == 1:
            time.sleep(1)
            print()
            print("Aguarde! computador escolhendo a palavra...")
            time.sleep(3)
            print()
            print("Palavra escolhida com sucesso. Boa Sorte!")
            time.sleep(1)
            print()

            with open('animal.txt', 'r') as arquivo:
                linhas = arquivo.read()
                animais = linhas.split('\n')

            palavra = choice(animais).upper()

            forca = """
            ____
                |
               ---"""
    
            vazio = """ 

            """

            cabeca = """
                O

            """

            tronco = """
                O
                |
            """

            braco_esquerdo = """
                O
               /|
            """

            braco_direito = """
                O
               /|\\ 
            """

            perna_esquerda = """
                O
               /|\\
               /
            """

            perna_direita = """
                O
               /|\\
               / \\
            """

            personagem = [
            vazio,
            cabeca,
            tronco,
            braco_esquerdo,
            braco_direito,
            perna_esquerda,
            perna_direita,
            ]

            acertos = 0
            erros = 0
            letras_acertadas = ""
            letras_erradas = ""

            while acertos != len(palavra) and erros != 7:
                mensagem = ''
                for letra in palavra:
                    if letra in letras_acertadas:
                        mensagem += f"{letra} "
                    else:
                        mensagem += "- "
                print(mensagem)
                print(forca+personagem[erros])
                print(f"Letras já digitadas:  {letras_erradas}" + " ")
                print()

                letra = input("Digite a letra: ").upper()
                print()

                if letra in letras_acertadas+letras_erradas:
                    print("Letra já foi escolhida")
                    print()
                    continue

                if letra in palavra:
                    print("Você acertou a letra")
                    letras_acertadas += letra
                    acertos += palavra.count(letra)
                    print()
                else:
                    print("Que pena! você errou a letra")
                    letras_erradas += letra
                    erros += 1
                    print()
            if (acertos == len(palavra)):
                vencedor()
            else:
                perdedor()
        if tipo == 2:
            time.sleep(1)
            print()
            print("Aguarde! computador escolhendo a palavra...")
            time.sleep(3)
            print()
            print("Palavra escolhida com sucesso. Boa Sorte!")
            time.sleep(1)
            print()

            with open('vegetal.txt', 'r') as arquivo:
                linhas = arquivo.read()
                vegetais = linhas.split('\n')

            palavra = choice(vegetais).upper()

            forca = """
            ____
                |
               ---"""
    
            vazio = """ 

            """

            cabeca = """
                O

            """

            tronco = """
                O
                |
            """

            braco_esquerdo = """
                O
               /|
            """

            braco_direito = """
                O
               /|\\ 
            """

            perna_esquerda = """
                O
               /|\\
               /
            """

            perna_direita = """
                O
               /|\\
               / \\
            """

            personagem = [
            vazio,
            cabeca,
            tronco,
            braco_esquerdo,
            braco_direito,
            perna_esquerda,
            perna_direita,
            ]

            acertos = 0
            erros = 0
            letras_acertadas = ""
            letras_erradas = ""

            while acertos != len(palavra) and erros != 7:
                mensagem = ''
                for letra in palavra:
                    if letra in letras_acertadas:
                        mensagem += f"{letra} "
                    else:
                        mensagem += "- "
                print(mensagem)
                print(forca+personagem[erros])
                print(f"Letras já digitadas:  {letras_erradas}" + " ")
                print()

                letra = input("Digite a letra: ").upper()
                print()

                if letra in letras_acertadas+letras_erradas:
                    print("Letra já foi escolhida")
                    print()
                    continue

                if letra in palavra:
                    print("Você acertou a letra")
                    letras_acertadas += letra
                    acertos += palavra.count(letra)
                    print()
                else:
                    print("Que pena! você errou a letra")
                    letras_erradas += letra
                    erros += 1
                    print()
            if (acertos == len(palavra)):
                vencedor()
            else:
                perdedor()
        if tipo == 3:
            time.sleep(1)
            print()
            print("Aguarde! computador escolhendo a palavra...")
            time.sleep(3)
            print()
            print("Palavra escolhida com sucesso. Boa Sorte!")
            time.sleep(1)
            print()

            with open('cidade.txt', 'r') as arquivo:
                linhas = arquivo.read()
                cidades = linhas.split('\n')

            palavra = choice(cidades).upper()

            forca = """
            ____
                |
               ---"""
    
            vazio = """ 

            """

            cabeca = """
                O

            """

            tronco = """
                O
                |
            """

            braco_esquerdo = """
                O
               /|
            """

            braco_direito = """
                O
               /|\\ 
            """

            perna_esquerda = """
                O
               /|\\
               /
            """

            perna_direita = """
                O
               /|\\
               / \\
            """

            personagem = [
            vazio,
            cabeca,
            tronco,
            braco_esquerdo,
            braco_direito,
            perna_esquerda,
            perna_direita,
            ]

            acertos = 0
            erros = 0
            letras_acertadas = ""
            letras_erradas = ""

            while acertos != len(palavra) and erros != 7:
                mensagem = ''
                for letra in palavra:
                    if letra in letras_acertadas:
                        mensagem += f"{letra} "
                    else:
                        mensagem += "- "
                print(mensagem)
                print(forca+personagem[erros])
                print(f"Letras já digitadas:  {letras_erradas}" + " ")
                print()

                letra = input("Digite a letra: ").upper()
                print()

                if letra in letras_acertadas+letras_erradas:
                    print("Letra já foi escolhida")
                    print()
                    continue

                if letra in palavra:
                    print("Você acertou a letra")
                    letras_acertadas += letra
                    acertos += palavra.count(letra)
                    print()
                else:
                    print("Que pena! você errou a letra")
                    letras_erradas += letra
                    erros += 1
                    print()
            if (acertos == len(palavra)):
                vencedor()
            else:
                perdedor()
        if tipo == 4:
            time.sleep(1)
            print()
            print("Aguarde! computador escolhendo a palavra...")
            time.sleep(3)
            print()
            print("Palavra escolhida com sucesso. Boa Sorte!")
            time.sleep(1)
            print()

            with open('linguagem.txt', 'r') as arquivo:
                linhas = arquivo.read()
                linguagens = linhas.split('\n')

            palavra = choice(linguagens).upper()

            forca = """
            ____
                |
               ---"""
    
            vazio = """ 

            """

            cabeca = """
                O

            """

            tronco = """
                O
                |
            """

            braco_esquerdo = """
                O
               /|
            """

            braco_direito = """
                O
               /|\\ 
            """

            perna_esquerda = """
                O
               /|\\
               /
            """

            perna_direita = """
                O
               /|\\
               / \\
            """

            personagem = [
            vazio,
            cabeca,
            tronco,
            braco_esquerdo,
            braco_direito,
            perna_esquerda,
            perna_direita,
            ]

            acertos = 0
            erros = 0
            letras_acertadas = ""
            letras_erradas = ""

            while acertos != len(palavra) and erros != 7:
                mensagem = ''
                for letra in palavra:
                    if letra in letras_acertadas:
                        mensagem += f"{letra} "
                    else:
                        mensagem += "- "
                print(mensagem)
                print(forca+personagem[erros])
                print(f"Letras já digitadas:  {letras_erradas}" + " ")
                print()

                letra = input("Digite a letra: ").upper()
                print()

                if letra in letras_acertadas+letras_erradas:
                    print("Letra já foi escolhida")
                    print()
                    continue

                if letra in palavra:
                    print("Você acertou a letra")
                    letras_acertadas += letra
                    acertos += palavra.count(letra)
                    print()
                else:
                    print("Que pena! você errou a letra")
                    letras_erradas += letra
                    erros += 1
                    print()
            if (acertos == len(palavra)):
                vencedor()
            else:
                perdedor()
    else:
        time.sleep(1)
        print()
        print("Obrigado e volte sempre!")
        print()
        break

