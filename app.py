import random 

def conversor():
    moedas = {
        "usd": 5.0,
        "eur": 5.5,
        "gbp": 6.7,
        "jpy": 0.031,
    }
    
    print("\n================== TUTORIAL ==================")
    print("1 - Digite o valor em Reais (R$)")
    print("2 - Escolha a moeda para conversão")
    print("==============================================")
    
    while True:
        print("\n===== CONVERSOR DE MOEDAS =====") 
        try:
            valor = float(input("Digite o valor (R$): "))
        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números (use ponto para decimais).")
            continue

        moeda = input("Escolha a moeda (USD, EUR, GBP, JPY): ").lower().strip()

        if moeda not in moedas:
            print(f"[ERRO] Moeda '{moeda.upper()}' inválida ou não suportada.")
            continue

        resultado = valor / moedas[moeda]
        print(f"\n[SUCESSO] Valor convertido: {resultado:.2f} {moeda.upper()}")

        pergunta = input("\nDeseja fazer outra conversão? (sim/não): ").strip().lower()
        if pergunta in ["não", "nao", "n"]:
            break

def calculadora():
    print("\n================== TUTORIAL ==================")
    print("1 - Digite os dois números desejados")
    print("2 - Escolha uma das operações: +, -, *, /, **")
    print("Nota: Use ponto (.) para números decimais (ex: 2.5)")
    print("==============================================")

    while True:
        print("\n===== CALCULADORA =====")
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números.")
            continue

        operacao = input("Escolha a operação (+, -, *, /, **): ").strip()

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
                    print("[ERRO] Divisão por zero não é permitida.")
                    valido = False
                else:
                    res = num1 / num2
                    print(f"O resto dessa divisão é: {num1 % num2}")
            case "**":
                try:
                    res = num1 ** num2
                except OverflowError:
                    print("[ERRO] O resultado desta potência é grande demais para o sistema.")
                    valido = False
            case _:
                print(f"[ERRO] Operação '{operacao}' inválida. Use apenas +, -, *, /, **.")
                valido = False

        if valido:
            print(f"\n[SUCESSO] O resultado é: {res}")

        opcao_calc = input("\nDeseja fazer mais contas? (sim/não): ").strip().lower()
        if opcao_calc in ["não", "nao", "n"]:
            break

def adivinhacao():
    while True: 
        num_jog = random.randint(1, 1000) 

        print("\n================== TUTORIAL ==================")
        print("1 - Tente adivinhar o número secreto entre 1 e 1000")
        print("2 - Você tem um limite de 10 tentativas")
        print("==============================================")

        acertou = False
        for i in range(10):
            print(f"\n===== JOGO DE ADIVINHAÇÃO (Tentativa {i+1}/10) =====")
            try:
                opcao_jog = int(input("Digite seu palpite: ")) 
            except ValueError:
                print("[ERRO] Entrada inválida. Digite apenas números inteiros.")
                continue

            if opcao_jog > num_jog: 
                print("Dica: O número secreto é MENOR.") 
            elif opcao_jog < num_jog: 
                print("Dica: O número secreto é MAIOR.") 
            else: 
                print("\n🎉 [SUCESSO] PARABÉNS! VOCÊ ACERTOU O NÚMERO SECRETO!! 🎉") 
                acertou = True
                break 

            print(f"Tentativas restantes: {10 - (i + 1)}")

        if not acertou:
            print(f"\n[FIM DE JOGO] Suas chances acabaram! O número era: {num_jog}")

        opcao2 = input("\nDeseja jogar mais uma rodada? (sim/não): ").strip().lower()
        if opcao2 in ["não", "nao", "n"]: 
            break

def game():
    opcoes = ["pedra", "papel", "tesoura"]

    print("\n================== TUTORIAL ==================")
    print("1 - Escolha entre: pedra, papel ou tesoura")
    print("2 - Vença o computador na disputa!")
    print("==============================================")

    while True:
        print("\n===== PEDRA, PAPEL E TESOURA =====")
        computador = random.choice(opcoes)
        jogador = input("Escolha sua jogada: ").lower().strip()

        if jogador not in opcoes:
            print("[ERRO] Jogada inválida. Escolha apenas 'pedra', 'papel' ou 'tesoura'.")
            continue

        print(f"\nComputador escolheu: {computador.upper()}")
        print(f"Você escolheu: {jogador.upper()}")

        if jogador == computador:
            print("Resultado: Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Resultado: 🎉 Você venceu!")
        else:
            print("Resultado: 😢 Você perdeu!")

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
            opcao_jogo = int(input("Escolha uma opção (1-3): "))
        except ValueError:
            print("[ERRO] Entrada inválida. Por favor, digite apenas números.")
            continue

        if opcao_jogo == 1:
            adivinhacao()
        elif opcao_jogo == 2:
            game()
        elif opcao_jogo == 3:
            break
        else:
            print(f"[ERRO] Opção {opcao_jogo} indisponível. Escolha um número de 1 a 3.")

def utilidades():
    while True:
        print("\n===== UTILIDADES =====")
        print("1) Calculadora")
        print("2) Conversor de Moedas")
        print("3) Voltar ao Menu Principal")

        try:
            opcao_utilidades = int(input("Escolha uma opção (1-3): "))
        except ValueError:
            print("[ERRO] Entrada inválida. Por favor, digite apenas números.")
            continue

        if opcao_utilidades == 1:
            calculadora()
        elif opcao_utilidades == 2:
            conversor()
        elif opcao_utilidades == 3:
            break
        else:
            print(f"[ERRO] Opção {opcao_utilidades} indisponível. Escolha um número de 1 a 3.")

def menu(): 
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1) Jogos")
        print("2) Utilidades")
        print("3) Sair do Programa")

        try:
           opcao_menu = int(input("Escolha uma opção (1-3): "))
        except ValueError:
           print("[ERRO] Entrada inválida. Por favor, digite apenas números.")
           continue

        if opcao_menu == 1:
            jogos()
        elif opcao_menu == 2:
            utilidades()
        elif opcao_menu == 3:
            print("\n[SUCESSO] Obrigado por utilizar o programa. Até logo!")
            break
        else:
            print(f"[ERRO] Opção {opcao_menu} inválida. Escolha um número de 1 a 3.")

if __name__ == "__main__":
    menu()
