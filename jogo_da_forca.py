from random import choice
import time

def titulo(mensagem, simbolo="-="):
    print()
    print(simbolo*15)
    print(mensagem)
    print(simbolo*15)

def jogadorVenceu():
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

def jogadorPerdeu():
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

def listaNomesAnimais():
    time.sleep(1)
    print()
    print("Aguarde! computador escolhendo a palavra...")
    time.sleep(3)
    print()
    print("Palavra escolhida com sucesso. Boa Sorte!")
    time.sleep(1)
    print()

    with open('animal.txt', 'r') as arquivoAnimal:
            linhasArquivoAnimal = arquivoAnimal.read()
            listaDeAnimais = linhasArquivoAnimal.split('\n')
    
    global palavraSorteada
    
    palavraSorteada = choice(listaDeAnimais).upper()

def listaNomesVegetais():
    time.sleep(1)
    print()
    print("Aguarde! computador escolhendo a palavra...")
    time.sleep(3)
    print()
    print("Palavra escolhida com sucesso. Boa Sorte!")
    time.sleep(1)
    print()

    with open('vegetal.txt', 'r') as arquivoVegetal:
        linhasArquivoVegetal = arquivoVegetal.read()
        listaDeVegetais = linhasArquivoVegetal.split('\n')
    
    global palavraSorteada

    palavraSorteada = choice(listaDeVegetais).upper()

def listaNomesCidades():
    time.sleep(1)
    print()
    print("Aguarde! computador escolhendo a palavra...")
    time.sleep(3)
    print()
    print("Palavra escolhida com sucesso. Boa Sorte!")
    time.sleep(1)
    print()

    with open('cidade.txt', 'r') as arquivoCidade:
        linhasArquivoCidade = arquivoCidade.read()
        listaDeCidades = linhasArquivoCidade.split('\n')
    
    global palavraSorteada

    palavraSorteada = choice(listaDeCidades).upper()

def listaNomesLinguagens():
    time.sleep(1)
    print()
    print("Aguarde! computador escolhendo a palavra...")
    time.sleep(3)
    print()
    print("Palavra escolhida com sucesso. Boa Sorte!")
    time.sleep(1)
    print()

    with open('linguagem.txt', 'r') as arquivoLinguagem:
        linhasArquivoLinguagem = arquivoLinguagem.read()
        listaDeLinguagens = linhasArquivoLinguagem.split('\n')
    
    global palavraSorteada

    palavraSorteada = choice(listaDeLinguagens).upper()

def estruturaELogicaDoJogo():

    global palavraSorteada
    global numeroDeAcerto

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

    numeroDeAcerto = 0
    numeroDeErro = 0
    letraCorreta = ""
    letraErrada = ""

    while numeroDeAcerto != len(palavraSorteada) and numeroDeErro != 7:

        mensagem = ''

        for letraEscolhida in palavraSorteada:

            if letraEscolhida in letraCorreta:
                mensagem += f"{letraEscolhida} "

            if letraEscolhida not in letraCorreta:
                mensagem += "- "

        print(mensagem)
        print(forca+personagem[numeroDeErro])
        print(f"Letras já digitadas:  {letraErrada}" + " ")
        print()

        letraEscolhida = input("Digite a letra: ").upper()
        print()

        if letraEscolhida in letraCorreta + letraErrada:
            print(f"Letra '{letraEscolhida}' já foi escolhida")
            print()
            continue

        if letraEscolhida in palavraSorteada:
            print("Você acertou a letra")
            letraCorreta += letraEscolhida
            numeroDeAcerto += palavraSorteada.count(letraEscolhida)
            print()

        if letraEscolhida not in palavraSorteada:
            print("Que pena! você errou a letra")
            letraErrada += letraEscolhida
            numeroDeErro += 1
            print()

        if (numeroDeAcerto == len(palavraSorteada)):
            print(f"A palavra sorteada foi: {palavraSorteada}")
            print()
            jogadorVenceu()
        
        if (numeroDeErro > 6):
            print(f"A palavra sorteada foi: {palavraSorteada}")
            print()
            jogadorPerdeu()

while True:
    time.sleep(1)
    titulo("JOGO DA FORCA", "-=")
    time.sleep(1)
    print("[1] JOGAR")
    print("[2] SAIR")
    opcaoMenuInicial = int(input("OPÇÃO: "))
    if opcaoMenuInicial == 1:
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
        escolherAssunto = int(input("OPÇÃO: "))
        if escolherAssunto == 1:
            listaNomesAnimais()
            estruturaELogicaDoJogo()
        if escolherAssunto == 2:
            listaNomesVegetais()
            estruturaELogicaDoJogo()
        if escolherAssunto == 3:
            listaNomesCidades()
            estruturaELogicaDoJogo()
        if escolherAssunto == 4:
            listaNomesLinguagens()
            estruturaELogicaDoJogo()
    else:
        time.sleep(1)
        print()
        print("Obrigado e volte sempre!")
        print()
        break

