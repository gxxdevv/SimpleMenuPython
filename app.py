import random 

def conversor():
    moedas ={
        "usd": 5.0,
        "eur": 5.5,
        "gbp": 6.7,
    }
    while True:
        print("\n=====CONVERSOR=====") 
        try:
            valor = float(input("digite o valor a ser convertido em BRL: R$"))
        except ValueError:
            print("só números")
            continue

        moeda = input("Escolha a moeda (USD, EUR, GBP): ").lower().strip()

        if moeda not in moedas:
            print("Moeda inválida")
            continue
        
        resultado = valor / moedas[moeda]
        print(f"Valor convertido: {resultado:.2f} {moeda.upper()}")
        
        pergunta = input("deseja fazer mais alguma comversão? ")
        if pergunta.strip().lower() in ["não", "nao"]:
            print("adeus!")
            break

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
                try:
                    res = num1 ** num2
                except OverflowError:
                    print("número grande demais!")
                    continue

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
        num_jog = random.randint(1,1000) 

        for i in range(10):
            print("\n=====ADIVINHAÇÃO=====")
            try:
                opcao_jog = int(input("Vamos ver se você acerta o número: ")) 
            except ValueError:
                print("Digite apenas números!")
                continue
            
            if opcao_jog > num_jog: 
                print("número menor") 
            elif opcao_jog < num_jog: 
                print("número maior") 
            else: 
                print("ACERTOU!!") 
                break 
            
            print(f"tentativas restantes: {9 - i}")
        
        else:
            print("Perdeu!")

        opcao2 = input("deseja jogar mais uma rodada?") 
        if opcao2.strip().lower() in ["não","nao"]: 
            print("Adeus, volte sempre!") 
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

def jogos():
    while True:
        print("\n=====JOGOS=====")
        print("1) jogo de adivinhação")
        print("2) pedra, papel e tesoura")
        print("3) sair")

        try:
            opcao_jogo = int(input("Escolha uma opção: "))
        except ValueError:
            print("somente números")
            continue

        if opcao_jogo == 1:
            adivinhacao()
        elif opcao_jogo == 2:
            game()
        elif opcao_jogo == 3:
            break
        else:
            print("Em Breve...")
            continue
 
def utilidades():
    while True:
        print("\n=====UTILIDADES=====")
        print("1) calculadora")
        print("2) conversor de moedas")
        print("3) sair")

        try:
            opcao_utilidades = int(input("Escolha uma opção: "))
        except ValueError:
            print("somente números")
            continue

        if opcao_utilidades == 1:
            calculadora()
        elif opcao_utilidades == 2:
            conversor()
        elif opcao_utilidades == 3:
            break
        else:
            print("Em Breve...")
            continue

def menu(): 
    while True:
        print("\n=====MENU=====")
        print("1) Jogos")
        print("2) Utilidades")
        print("3) Sair")

        try:
           opcao_menu = int(input("Escolha uma opção: "))
        except ValueError:
           print("somente números")
           continue

        if opcao_menu == 1:
            jogos()
        elif opcao_menu == 2:
            utilidades()
        elif opcao_menu == 3:
            print("adeus")
            break
        else:
            print("Em breve...")
            continue

if __name__ == "__main__":
    menu()
