import operator

Conta_desejada = {
    1: {"nome": "Multiplicação", "funcao": operator.mul},
    2: {"nome": "Divisão", "funcao": operator.truediv},
    3: {"nome": "Subtração", "funcao": operator.sub},
    4: {"nome": "Adição", "funcao": operator.add},
    5: {"nome": "Sair", "funcao": None}
}

print('Bem vindo a calculadora!')

# 1. O loop principal começa aqui
while True:
    print("\nO que deseja fazer?")
    for id_prod, dados in Conta_desejada.items():
        print(f" {id_prod} - {dados['nome']}")
    
    try:
        Ação_escolhida = int(input('\nDigite o número da ação: '))
        
        # 2. Verifica primeiro se a escolha foi a de Sair (opção 5)
        if Ação_escolhida == 5:
            print('\nSaindo da calculadora... Até mais!')
            break # Quebra o loop e encerra o programa
            
        if Ação_escolhida in Conta_desejada:
            Conta = Conta_desejada[Ação_escolhida]
            Número1 = int(input("Digite o primeiro número: "))
            Número2 = int(input("Digite o segundo número: "))
            
            # Executa o cálculo usando a Tabela de Despacho
            funcao_calculo = Conta["funcao"]
            resultado = funcao_calculo(Número1, Número2)
            print(f"\nO resultado da {Conta['nome']} é: {resultado}")
            
            # 3. Pergunta se o usuário quer fazer outro cálculo
            continuar = input("\nDeseja fazer outro cálculo? (S/N): ").strip().upper()
            if continuar != 'S':
                print('\nSaindo da calculadora... Até mais!')
                break # Quebra o loop e encerra o programa
                
        else:
            print('\nOpção inválida! Escolha um número de 1 a 5.')
            
    except ValueError:
        print('\nErro: Por favor, digite apenas números inteiros.')
    except ZeroDivisionError:
        print('\nErro: Não é possível dividir por zero. Tente novamente.')