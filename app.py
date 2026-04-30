import random 

def calculadora():
    while True:
        print("\n=====CALCULADORA=====")
        print("+ soma")
        print("- subtração")
        print("/ divisão")
        print("* multiplicação")
        print("** exponenciação")
        
        try:
            num1 = float(input("digite um número: "))
            num2 = float(input("digite outro número: "))
        except ValueError:
            print("Só números")
            continue

        operacao = input("Que tipo de conta deseja fazer? ")
        
        match operacao:
            case "+":
                res = num1 + num2

            case "-":
                res = num1 - num2

            case "*":
                res = num1 * num2

            case "/":
                if num2 == 0:
                    print("não existe divisão por 0")
                    continue
                else:
                    res = num1 / num2
                    print(f"o resto dessa divisão é {num1 % num2}")

            case "**":
                res = num1 ** num2

            case _:
                print("operação inválida")
                continue
        
        print(f"o resultado é {res}")
        
        opcao_calc = input("deseja fazer mais contas? ")
        
        if opcao_calc.strip().lower() in ["não", "nao"]:
            print("adeus!")
            break

def adivinhacao():
  while True:
    num = random.randint(1,1000)
    print("\n=====GAME=====")
    contador = 10
    for i in range(contador):
        try:
            opcao = int(input("Digite seu palpite: "))
        except ValueError:
            print("somente números!")
            continue
        
        if opcao > num:
            print("número menor")
            print(f"tentativas restantes: {contador}")
        elif opcao < num:
            print("número maior")
            print(f"número de tentativas: {contador}")
        else:
            print("ACERTOU!")
            break
        
        print(f"tentativas restantes: {contador - i - 1}")
    else:
        print("Perdeu!")
    
    opcao2 = input("jogar novamente? ")
    if opcao2.strip().lower() in ["não", "nao"]:
        print("Valeu por jogar!")
        break

def game():
    opcoes = ["pedra", "papel", "tesoura"]

    print("\n=====GAME=====")
    print("Olá jogador(a), vamos jogar pedra, papel e tesoura")

    while True:
        computador = random.choice(opcoes)
        jogador = input("Escolha: ").lower().strip()

        if jogador not in opcoes:
            print("Opção inválida")
            continue

        print(f"Computador escolheu {computador}")
        print(f"Você escolheu {jogador}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):
            print("Você venceu!")
        else:
            print("Você Perdeu!")

        pergunta = input("Deseja jogar de novo? ").lower().strip()

        if pergunta.strip().lower() in ["não", "nao"]:
            print("Adeus")
            break 
          
def menu():
    while True:
        print("\n=====MENU=====")
        print("1) usar a calculadora?")
        print("2) jogar um jogo de adivinhação?")
        print("3) Jogar Pedra, papel e tesoura?")
        print("4) sair do programa?")
        
        try:
            opcao_menu = int(input("Digite sua escolha: "))
        except ValueError:
            print("Somente núneros")
            continue

        if opcao_menu == 1:
            calculadora()
        elif opcao_menu == 2:
            adivinhacao()
        elif opcao_menu == 3:
            game()
        elif opcao_menu == 4:
            print("Adeus!")
            break
 
if __name__ == "__main__":
    menu()
