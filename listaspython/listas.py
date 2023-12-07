# Tarefa

"""Faça um algoritmo que leia até 30 números inteiros quaisquer.
Utilize as seguintes variáveis: listaA, listaB e listaC
Para cada número inteiro lido, verificar: 
Caso o número seja negativo, dar a seguinte mensagem: "Digite apenas números positivos" e ler o próximo.
Caso o número seja 0(zero), ou chegue a 30 números digitados, finalize a digitação (mesmo que a quantidade de números digitados seja menor que 30) e mostre o conteúdo das 3 listas, imprimindo os elementos de cada lista individualmente.
Caso o número seja positivo faça:
- verifique se o número está entre 10 e 30. Se sim, adicione esse número na listaA
- verifique se o número está entre 50 e 70. Se sim, adicione esse número na listaB
- verifique se o número está entre 20 e 60. Se sim, adicione esse número na listaC
- quando alguma das listas estiver com 5 elementos, apague todos os elementos desta lista...
"""

ListaA = [] # Variável da ListaA
ListaB = [] # Variável da ListaB
ListaC = [] # Variável da ListaC
count = 0 # Variável para a contagem de números limite de leitura
max_count = 5 # Variável para a contagem de números limite da lista

for x in range(30):
    try:
        num = int(input("Digite um número: "))
    except ValueError:
        print("Insira um número inteiro!")
        continue  # Continua pedindo um número válido
    
    if num < 0:
        print("Digite números positivos!")
    
    if num > 10 and num < 30:
        if len(ListaA) < max_count:
            ListaA.append(num)
            print("Número {} adicionado na ListaA".format(num)) 
            # Se o número estiver entre 10 e 30 adiciona na ListaA.
             
    if num > 50 and num < 70:
        if len(ListaB) < max_count:
            ListaB.append(num)
            print("Número {} adicionado na ListaB".format(num))  
            # Se o número estiver entre 50 e 70 adiciona na ListaB. 
        
    if num > 20 and num < 60:
        if len(ListaC) < max_count:
            ListaC.append(num)
            print("Número {} adicionado na ListaC".format(num))
            # Se o número estiver entre 20 e 60 adiciona na ListaB.       
             
    elif num == 0:
        print("Encerrando o programa.")
        break
        # Número 0: Sair do programa


    if len(ListaA) == max_count:
            ListaA.clear()
            print("Limite atingido ListaA sendo limpa.")  
    if len(ListaB) == max_count:
            ListaB.clear()
            print("Limite atingido ListaB sendo limpa.")
    if len(ListaC) == max_count:
            ListaC.clear()
            print("Limite atingido ListaB sendo limpa.")           
    # Verifica se a lista chegou a 5 elementos e limpa a lista.
   
    count += 1
    # Adiciona um número digitado a variável "count"
         
    
if count == 30:
    print("Limite atingido. \nEncerrando programa.")
    # Quando a contagem atingir 30 números encerra o programa.

if not ListaA:
    print("ListaA está vazia.\n")
else:
    print("\nListaA:")
    for item in ListaA: 
        print(item)

if not ListaB:
    print("ListaB está vazia.\n")
else:
    print("\nListaB:")
    for item in ListaB: 
        print(item)

if not ListaC:
    print("ListaC está vazia.\n")
else:
    print("\nListaC:")
    for item in ListaC: 
        print(item)
        
# Vai verificar se está na lista ou não