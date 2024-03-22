# VARIÁVEIS GLOBAIS:
personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara

# MENU:
def menu():
    i = "0"

    while i != "2":
        print("Bem vindo a humanos vs capivaras")
        print("""
    Menu:
            1- Jogar
            2- Sair
            """)
        i = input()
            
        if i == "1":
            startJogo()
            
        elif i == "2":
            print("Saindo do jogo...")
            
        else:
            print("Comando inválido")

# SELECIONAR CLASSE DO PERSONAGEM:
def selecionarClasse():
    global personagemClasse
    print("""
    Selecione sua classe:
        1 - Humano      2 - Capivara

    """)
    personagemClasse = input()
        
    if personagemClasse == "1":
        print("Você selecionou a classe Humano.")

    elif personagemClasse == "2":
        print("Você selecionou a classe Capivara.")

# ESCOLHER OPÇÃO BATALHA:
def opcaoBatalha():
    print("""
1 - ATACAR      2 - USAR ITEM       3 - FUGIR
""")
    
    i = input()

    if i == "1" or i == "2" or i == "3":
        return i
    
    else:
        print("Opção inválida...")
        opcaoBatalha()
    
# BATALHA HUMANO CONTRA CAPIVARA:
def batalhaHumano():
    jogadorEscolha = "0"
    print("Você encontra uma Capivara Selvagem, o que você faz?")
    jogadorEscolha = opcaoBatalha()
    print(f"A escolha do jogador foi {jogadorEscolha}")

# COMEÇAR O JOGO:
def startJogo():
    selecionarClasse()
    
    if personagemClasse == "1":
        batalhaHumano()
    
    elif personagemClasse == "2":
        batalhaCapivara()

    else:
        print("Opção inválida...")
        selecionarClasse()

# MAIN():       
menu()


-----------------------------------------------------------------------------------------------------------------------------



import random

vida_cap = 10
vida_hum = 10



print("-----------------------------------------------------------" )
print("-----------------------------------------------------------" )
print("-----------------------------------------------------------" )
print("-----------------------------------------------------------" )
print("------------------HUMAN  X  CAPIVARA-----------------------" )
print("_/﹋\_-----------------------------------------------------" )
print("(҂`_´)--------------------------------------^..^____/------" )
print("<;︻╦╤─ *-*-*-*-*-*-*-*-*-*------------------\./ ___)------" )
print("-----------------------------------------------||  || -----" )
print("\n")
print("\n")
print("\n")


player = int(input("Você é 1-humano ou 2-Capivara? "))

if player == 1:
    print("Você é um Humano explorando o mundo")
    print("Apareceu uma capivara mutante e faminta por sangue humano")
    print("--^..^____/--")
    print("---\./ ___)--")
    print("-----||  ||--")
    player1 = "Humano"
    player2 = "capivara"
else:
    print("Você é uma Capivara mutante sedenta por sangue humano")
    print("Apareceu um humano, mas não parece ser uma presa fácil.")
    print("_/﹋\_")
    print("(҂`_´")
    print("<;︻╦╤─")
    player1 = "Capivara"
    player2 = "Humano"

while vida_hum > 0 and vida_cap > 0:
    print("Life Human: ", vida_hum)
    print("Life Capivara: ", vida_cap)
    
    if player == 1:
        input("Aperte enter para o ataque")
        dano = random.randint(1, 2)
        print("{} deu {} de dano!".format(player1, dano))
        vida_cap -= dano
    else:
        input("Aperte enter para o ataque")
        dano = random.randint(1, 2)
        print("{} deu {} de dano!".format(player2, dano))
        vida_hum -= dano

player = 1 if player == 2 else 2
