import random 

def conversor():
    moedas ={
        "usd": 5.0,
        "eur": 5.5,
        "gbp": 6.7,
        "jpy": 0.031,
    }
    print("\n=====TUTORIAL=====")
    print("1- Digite o valor a ser convertido")
    print("2- Escolha a moeda a qual deseja converter (USD, EUR, GBP, JPY)")
    
    while True:
        print("\n=====CONVERSOR=====") 
        try:
            valor = float(input("Digite o valor: R$"))
        except ValueError:
            print("Digite apenas números.")
            continue

        moeda = input("Escolha a moeda: ").lower().strip()

        if moeda not in moedas:
            print("Moeda inválida.")
            continue

        resultado = valor / moedas[moeda]
        print(f"Valor convertido: {resultado:.2f} {moeda.upper()}")

        pergunta = input("\nDeseja fazer mais alguma conversão? (sim/não): ").strip().lower()
        if pergunta in ["não", "nao", "n"]:
            break

def calculadora():
    print("\n=====TUTORIAL=====")
    print("1- Digite os números desejados")
    print("2- Escolha UMA das operações (+, -, *, /, **)")
    print("IMPORTANTE: Para usar vírgula na sua conta, digite o ponto (.)")

    while True:
        print("\n=====CALCULADORA=====")
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Apenas números são aceitos.")
            continue

        operacao = input("Que tipo de conta deseja fazer? ").strip()

        # Bug corrigido: isolando a execução para evitar NameError no print final
        valido = True
        match operacao:
            case "+":
                res = num1 + num2
            case "-":
                res = num1 - num2
            case "*":
                res = num1 * num2
            case "/":
                if num2 == 0:
                    print("Erro: Não existe divisão por 0.")
                    valido = False
                else:
                    res = num1 / num2
                    print(f"O resto dessa divisão é: {num1 % num2}")
            case "**":
                try:
                    res = num1 ** num2
                except OverflowError:
                    print("Resultado grande demais para o sistema!")
                    valido = False
            case _:
                print("Operação inválida.")
                valido = False

        if valido:
            print(f"O resultado é: {res}")

        opcao_calc = input("\nDeseja fazer mais contas? (sim/não): ").strip().lower()
        if opcao_calc in ["não", "nao", "n"]:
            break

def adivinhacao():
    while True: 
        num_jog = random.randint(1, 1000) 

        print("\n=====TUTORIAL=====")
        print("1- Adivinhe o número secreto entre 1 e 1000")
        print("2- Você possui 10 tentativas")

        acertou = False
        for i in range(10):
            print(f"\n===== ADIVINHAÇÃO (Tentativa {i+1}/10) =====")
            try:
                opcao_jog = int(input("Palpite: ")) 
            except ValueError:
                print("Digite apenas números inteiros!")
                continue

            if opcao_jog > num_jog: 
                print("O número secreto é MENOR.") 
            elif opcao_jog < num_jog: 
                print("O número secreto é MAIOR.") 
            else: 
                print("🎉 PARABÉNS! VOCÊ ACERTOU!! 🎉") 
                acertou = True
                break 

            # Ajuste na contagem de tentativas restantes
            print(f"Tentativas restantes: {10 - (i + 1)}")

        if not acertou:
            print(f"\nQue pena, suas chances acabaram! O número era: {num_jog}")

        opcao2 = input("\nDeseja jogar mais uma rodada? (sim/não): ").strip().lower()
        if opcao2 in ["não", "nao", "n"]: 
            break

def game():
    opcoes = ["pedra", "papel", "tesoura"]

    print("\n=====TUTORIAL=====")
    print("1- Escolha entre pedra, papel ou tesoura")
    print("2- Vença o computador se puder!")

    while True:
        print("\n===== PEDRA, PAPEL E TESOURA =====")
        computador = random.choice(opcoes)
        jogador = input("Escolha sua jogada: ").lower().strip()

        if jogador not in opcoes:
            print("Opção inválida! Digite pedra, papel ou tesoura.")
            continue

        print(f"Computador escolheu: {computador}")
        print(f"Você escolheu: {jogador}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        pergunta = input("\nDeseja jogar de novo? (sim/não): ").lower().strip()
        if pergunta in ["não", "nao", "n"]:
            break 

def jogos():
    while True:
        print("\n===== SELEÇÃO DE JOGOS =====")
        print("1) Jogo de Adivinhação")
        print("2) Pedra, Papel e Tesoura")
        print("3) Voltar ao Menu Principal")

        try:
            opcao_jogo = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite somente números.")
            continue

        if opcao_jogo == 1:
            adivinhacao()
        elif opcao_jogo == 2:
            game()
        elif opcao_jogo == 3:
            break
        else:
            print("Opção indisponível.")

def utilidades():
    while True:
        print("\n===== UTILIDADES =====")
        print("1) Calculadora")
        print("2) Conversor de Moedas")
        print("3) Voltar ao Menu Principal")

        try:
            opcao_utilidades = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite somente números.")
            continue

        if opcao_utilidades == 1:
            calculadora()
        elif opcao_utilidades == 2:
            conversor()
        elif opcao_utilidades == 3:
            break
        else:
            print("Opção indisponível.")

def menu(): 
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1) Jogos")
        print("2) Utilidades")
        print("3) Sair do Programa")

        try:
           opcao_menu = int(input("Escolha uma opção: "))
        except ValueError:
           print("Por favor, digite somente números.")
           continue

        if opcao_menu == 1:
            jogos()
        elif opcao_menu == 2:
            utilidades()
        elif opcao_menu == 3:
            print("\nObrigado por utilizar o programa. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
