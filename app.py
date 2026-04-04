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
        #define o número aleatório do jogo
        num_jog = random.randint(1,1000)
        
        #serve para informar ao jogador o intervalo de números
        print("número natural(0,1,2,...) entre 1 e 1000")
        
        while True: #loop de tentativas
            try: #significa tentar. Então, o usuário só pode digitar números
                opcao_jog = int(input("Vamos ver se você acerta o número: "))    
            except ValueError: #isso impede do usuário digitar letras   
                print("digite apenas números!")
                continue #isso continua o código normalmente
                
                #serve como forma de dica para o jogador
                if opcao_jog > num_jog:
                    print("número menor")
                elif opcao_jog < num_jog:
                    print("número maior")
                else:
                    print("ACERTOU!!")
                    break
                
            #pergunta seo jogador deseja jogar mais uma partida
            opcao2 = input("deseja jogar mais uma rodada?")   
            if opcao2.strip().lower() in ["não","nao"]:
                print("Adeus, volte sempre!")
                break
              
def adeus():
    print("Muito obrigado por usar o programa. Adeus!")
      
def menu():
    while True:
        print("Bem-vindo(a)!")
        print("O que deseja fazer?")
        print("1) usar a calculadora?")
        print("2) jogar um joguinho?")
        print("3) sair do programa?")
        
        opcao_menu = float(input("digite 1, 2 ou 3: "))
        if opcao_menu == 1:
            calculadora()
        elif opcao_menu == 2:
            joguinho()
        elif opcao_menu == 3:
            adeus()
            break
        elif opcao_menu == 3.14:
            print("Calma... PI?")
            print("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
            print("Gustavo diz:  Muito obrigado a todos que usaram o programa, que Deus abençoe a vida de vocês!")
            break
    
if __name__ == "__main__":
    menu()