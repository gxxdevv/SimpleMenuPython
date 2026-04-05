import random 

def calculadora():
    while True:
        print("+ soma")
        print("- subtração")
        print("/ divisão")
        print("* multiplicação")
        
        num1 = float(input("digite um número: "))
        num2 = float(input("digite outro número: "))
        
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
            case _:
                print("operação inválida")
                continue
        
        print(f"o resultado é {res}")
        
        opcao_calc = input("deseja fazer mais contas? ")
        
        if opcao_calc.strip().lower() in ["não", "nao"]:
            print("adeus!")
            break

def joguinho():
  while True:
    num = random.randint(1,1000)
    
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
               
def menu():
    while True:
        print("Bem-vindo(a)!")
        print("O que deseja fazer?")
        print("1) usar a calculadora?")
        print("2) jogar um joguinho?")
        print("3) sair do programa?")
        
        opcao_menu = input("digite 1, 2 ou 3: ")
        if opcao_menu == "1":
            calculadora()
        elif opcao_menu == "2":
            joguinho()
        elif opcao_menu == "3":
            print("Muito obrigado por usar o programa. Adeus!")
            break
        elif opcao_menu == "3.14":
            print("Calma... PI?")
            print("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
            print("Gustavo diz:  Muito obrigado a todos que usaram o programa, que Deus abençoe a vida de vocês!")
            break
    
if __name__ == "__main__":
    menu()
