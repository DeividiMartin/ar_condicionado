#>>>>>>| TABELAS |<<<<<<<<<<<

#TABELA 1-RECINTO 
entre_andares = 16
sob_telhados = 22.33


#TABELA 2-JANELAS
sol_manha_com_cortina =  160 

sol_tarde_com_cortina =  212 

sol_manha_sem_cortina =  222

sol_tarde_sem_cortina =  410 

vidros_na_sombra      =  37


#TABELA 3-PORTAS
portas = 125

#TABELA 4 - PESSOAS
pessoas = 125



#TABELA 5 ---APARELHOS ELETRICOS

aparelhos_eletricos = 0.9

#>>>>>>>>>| FIM TABELAS |<<<<<<<<<<


#>>>>| Armazenamento dos valores finais das funções |<<<<

valor_vetor_recinto= []
valor_vetor_janela = []
valor_vetor_porta = []
valor_vetor_pessoas = []
valor_vetor_aparelhos = []

#>>>>| Fimrmazenamento dos valores finais das funções |<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>| FUNÇOES |<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#Funçao criada para que o input só aceite resposta de numeros Float e inteiros

def decimal(palavra, lugar = int, dot = '.'):
    lugar = palavra.find(dot)
    palavra_antes = str(palavra[:lugar])
    lugar = lugar+1
    palavra_depois = str(palavra[lugar:])
    if palavra_antes.isdigit() == True and palavra_depois.isdigit() == True:
        return(True)
    else:
        return(False)



#FUNÇÃO RECINTO ONDE FICA O CODIGO QUE FAZ O CALCULO DE GASTO EM Kcal/h DO RECINTO


def recinto():
    #CONFERENCIA SE O INPUT É S OU N
        while True:
                andares_telhados = input('''
                        
A sala tem ligação direta com o telhado? S para sim ou N para não: ''')
                if  andares_telhados == 'S' or andares_telhados == 's' or andares_telhados == 'N' or andares_telhados == 'n':
                        break
                else:
                        print ('Por favor escolha uma opção valida!')
                
        #CODIGO ONDE PEDE AS DIMENÇOES DO RECINTO E ANALISA SE NÃO É STR
        while True:
                sala_comprimento = input('  Informe quantos metros de comprimento o recinto possui: ')
                
                if sala_comprimento == '0' or sala_comprimento == '':
                        sala_comprimento = 'a'
                
                if decimal(sala_comprimento) == True:
                        break
                if sala_comprimento.isdigit() == True:
                        break
                        
                else:
                        print(' Por favor insira um número valido! ')
                        
        #CODIGO ONDE PEDE AS DIMENÇOES DO RECINTO E ANALISA SE NÃO É STR
        while True:
                sala_largura = input('  Informe quantos metros de largura o recinto possui: ')
                
                if sala_largura == '0' or sala_largura == '':
                        sala_largura = 'a'
                
                if decimal(sala_largura) == True:
                        break
                if sala_largura.isdigit() == True:
                        break
                        
                else:
                        print(' Por favor insira um número valido! ')
        
        
        #CODIGO ONDE PEDE AS DIMENÇOES DO RECINTO E ANALISA SE NÃO É STR
        while True:
                sala_altura = input('  Informe quantos metros de altura o recinto possui: ')
                
                if sala_altura == '0' or sala_altura == '':
                        sala_altura = 'a'
                
                if decimal(sala_altura) == True:
                        break
                if sala_altura.isdigit() == True:
                        break
                        
                else:
                        print(' Por favor insira um número valido! ')


        #Calculo para saber o volume do recinto (metros cubicos)
        sala_largura = float (sala_largura)
        sala_comprimento = float (sala_comprimento)
        sala_altura = float (sala_altura)
        
        valor_recinto_mc =  sala_comprimento*sala_altura*sala_largura

        if andares_telhados == 'S' or andares_telhados == 's':
                gasto_recinto = (valor_recinto_mc*sob_telhados)
                        
        elif andares_telhados == 'N' or andares_telhados == 'n':
                gasto_recinto = (valor_recinto_mc*entre_andares)
                        
                
        valor_vetor_recinto.append(gasto_recinto) 

        #CODIGO PARA DECIDIR SE O USUARIO SERA MANDADO PARA FUNÇÃO DE JANELAS OU PORTAS CASO NÃO POSSUA JANELA NO RECINTO
        while True:
            possui_ou_nao= input ('''
                            
 O recinto possui janelas?

 Escreva (S) para sim e (N) para não: ''')
            if  possui_ou_nao == 'S' or possui_ou_nao == 's' or possui_ou_nao == 'N' or possui_ou_nao == 'n':
                    break
            else:
                    print (' Por favor escolha uma opção valida!')

        if possui_ou_nao == 's' or possui_ou_nao == 'S':
            tabela_janela()
        else:
            possui_ou_nao == 'n' or possui_ou_nao == 'N'
            tabela_porta()
            
            
#FUNÇÃO JANELA ONDE FICA O CODIGO QUE FAZ O CALCULO DO GASTO Kcal/h BASEADO NAS JANELAS DO RECINTO CASO O RECINTO POSSUA

def tabela_janela(): 

            
    i = 1

    valores_largura = []

    largura_janela = 0

    valores_altura = []

    altura_janela = 0

    all_alturaxlargura = []

# input para o usuario informar o numero de janelas existente na sala e verificar se não é str    
    while True:
        numero_janelas = input('''
                                   
 Infore o número de janelas que o recinto possui: ''')
        if numero_janelas.isdigit():
            numero_janelas = int (numero_janelas)
            break
        else:
            print('''
 Por favor insira um numero valido! ''')
            

      

# loop para escolher a posição da janela
    while len(valores_largura) != numero_janelas :
        
# Escolha de onde se encontra a janela
        while True:
            escolha = str(input('''
                    
 Digite a seguir a alternativa que corresponda com a janela ''' + str(i) + ''': ''' '''      
            
 [1] A janela recebe sol na manhã, porem possui cortinas
 [2] A janela recebe sol na tarde, porem possui cortinas
 [3] A janela recebe sol na manhã, porem não possui cortinas
 [4] A janela recebe sol na tarde, porem não possui cortinas
 [5] A janela fica constantemente na sombra

 Informe a opção correspondente a sua janela ''' + str(i) +  ":  [1] [2] [3] [4] ou [5] : "))
            if escolha == '1' or escolha == '2' or escolha =='3' or escolha == '4' or escolha == '5':
                break
            else:
                print(''' 
 Por favor insira um numero valido!''')
        
        
        
        if  escolha == '1':
            valor_final_tabela= (sol_manha_com_cortina)
                
                
        elif escolha == '2':
            valor_final_tabela= (sol_tarde_com_cortina)
                

        elif escolha == '3':
            valor_final_tabela= (sol_manha_sem_cortina)
                
            
        elif escolha == '4':
            valor_final_tabela= ( sol_tarde_sem_cortina)
            
        elif escolha == '5':
            valor_final_tabela= (vidros_na_sombra)

            
            
        # Input para informar a largura da janela do usiario  
        #Assim que informar a largura ira verificar se não é uma letra para dar continuação 
        while True:
            largura_janela = input ( '  Informe quantos metros de largura a janela ' + str(i) + ' possui: ')
            
            if largura_janela == '0' or largura_janela == '':
                largura_janela = 'a'
            
            if decimal(largura_janela) == True:
                valores_largura.append ( largura_janela )
                break
            if largura_janela.isdigit() == True:
                valores_largura.append ( largura_janela )
                break
                
            else:
                print(' Por favor insira um número valido! ')

            
            
        # Ipunt para informar a altura da janela do usuario
        #Assim que informar a altura ira verificar se não é uma letra para dar continuação
        while True:
            altura_janela = input ( '  Informe quantos metros de largura a janela ' + str(i) + 'possui: ')
            
            if altura_janela == '0' or altura_janela == '':
                altura_janela = 'a'
            
            if decimal(altura_janela) == True:
                valores_altura.append ( altura_janela )
                break
            if altura_janela.isdigit() == True:
                valores_altura.append ( altura_janela )
                break
        
            else:
                print(' Por favor insira um número valido! ')
            
                
         
        # Calculo para obter o valor da janela em metro cubico   
        soma = float(altura_janela)* float(largura_janela)
        
        i = i + 1 
        
                       
        valor_final_tabela = valor_final_tabela*soma
        
        # Armazena o valor do vetor escolhido na variavel all_aturaxlargura
        all_alturaxlargura.append (valor_final_tabela)
        
    # Loop para somar o valor total de gasto                
    l = all_alturaxlargura
    
    carga_termica_janela = int(0)
        
    for i in range(len(l)): 
        carga_termica_janela += (l[i])
                   
    #Valor total da carga termica
    
    valor_vetor_janela.append (carga_termica_janela)
    
    tabela_porta()
    

#FUNÇÃO PORTA ONDE FICA O CODIGO QUE FAZ O CALCULO DE GASTO EM Kcal/h  BASEADO NA QUANTIDADE DE PORTAS DO RECINTO

def tabela_porta(): 
    
    i = 1

    valores_largura = []

    largura_porta = 0

    valores_altura = []

    altura_porta = 0

    total_alturaxlargura = []

            
    #codigo para armazerar os valors da porta e verificar se não sera digitado str  
    while True:
        numero_portas = input('''                                   
 Informe o número de portas que o recinto possui: ''')
        if numero_portas.isdigit():
            numero_portas = int (numero_portas)
            break
        else:
            print('''
 Por favor insira um numero valido! ''')  
            
    while len(valores_largura) != numero_portas :
        #verifica se não é uma str e armazena o resultado
        while True:
            altura_porta = input ( '  Informe quantos metros de altura a porta ' + str(i) + ' possui : ')
                    
            if altura_porta == '0' or altura_porta == '':
                altura_porta = 'a'
                    
            if decimal(altura_porta) == True:
                valores_altura.append ( altura_porta )
                break
            if altura_porta.isdigit() == True:
                valores_altura.append ( altura_porta )
                break
                
            else:
                print(' Por favor insira um número valido! ')
                
                

                
        #verifica se não é uma str e armazena o resultado        
        while True:
            largura_porta = input ( '  Informe quantos metros de altura a porta ' + str(i) + ' possui : ')
            
            if largura_porta == '0' or largura_porta == '':
                largura_porta = 'a'
            
            if decimal(largura_porta) == True:
                valores_largura.append ( largura_porta )
                break
            if largura_porta.isdigit() == True:
                valores_largura.append ( largura_porta )
                break
        
            else:
                print(' Por favor insira um número valido! ')
                
                
        #Calcula a porta em metros quadrados   
        alturaxlargura = float (altura_porta) * float(largura_porta)
        
        i = i + 1
        
        
          
        #apos ter o resultado final ira armazenar o falor    
        resultado = portas*alturaxlargura
            
        total_alturaxlargura.append (resultado)
            
            
    #soma todo o vetor     
    l = total_alturaxlargura
    soma = int(0)
    for i in range (len (l)) : 
        soma += (l [i] )
            


   #valor final tabela portas
    valor_vetor_porta.append (soma)
    
    tabela_pessoas()
    
    
#FUNÇÃO PESSOAS ONDE FICA O CODIGO QUE FAZ O CALCULO DE GASTO EM Kcal/h  BASEADO NA QUANTIDADE DE PRSSOAS NO RECINTO


def tabela_pessoas():
    while True:
        quantidade = input('''
                            
        
 Informe o numero de pessoas presentes no recinto: ''')
        if not quantidade.isalpha():
            quantidade = int(quantidade)
            break
        else:
            print( ' Por favor insira um numero valido!' )    
        
    valor_total_pessoas = pessoas*quantidade
    

    
    #valor final tabela pessoas 
    valor_vetor_pessoas.append (valor_total_pessoas)
    
                    
    tabela_watt_nominal()


#FUNÇÃO APARELHOS ELETRICOS ONDE FICA O CODIGO QUE FAZ O CALCULO DE GASTO EM Kcal/h  BASEADO NA QUANTIDADE DE WATT NOMINAL  DO  RECINTO

def tabela_watt_nominal():
    #confere se não é str
    while True:
        valor_nominal = input ('''
                                    
 Informe número watts dos aparelhos elétricos que existam no local: ''')
        
        if  valor_nominal == '':
            valor_nominal = 'a'
        
        if decimal(valor_nominal) == True:
            break
        if valor_nominal.isdigit() == True:
            break
            
        else:
            print(' Por favor insira um número valido! ')
    #converte para float       
    valor_nominal = float (valor_nominal)
    #calcula o resultado final
    valor_aparelhos = valor_nominal*aparelhos_eletricos
    
    #valor final tabela aparelho armazenada
    valor_vetor_aparelhos.append (valor_aparelhos)
    
    final()
    
    
#FUNÇÃO FINAL ONDE FAZ O CALCULO DE Kcal/h PARA Btu BASEADO NO RESULTADOS DAS FUNÇOES NECESSARIAS PARA OBTER O RESULTADO 


def final():
    #Armazenamento dos resultados finais das funções
    print ('''
 
 RESULTADO DO LEVANTAMENTO:
 ''')


    carga_total_recinto = (valor_vetor_recinto [int(0)])
    print (' 1) Recinto: ' ,carga_total_recinto, ' Kcal/h')


    carga_total_janelas = (valor_vetor_janela [int(0)])
    print (' 2) Janelas: ',carga_total_janelas, ' Kcal/h')


    carga_total_portas = (valor_vetor_porta [int(0)])
    print (' 3) Portas: ',carga_total_portas, ' Kcal/h') 

    carga_total_pessoas = (valor_vetor_pessoas [int(0)])
    print (' 4) Pessoas: ',carga_total_pessoas, ' Kcal/h')

    carga_total_aparelhos = (valor_vetor_aparelhos [int(0)])
    print (' 5) Aparelhos elétricos: ',carga_total_aparelhos, ' Kcal/h')

    total_carga_termica_final =  carga_total_recinto + carga_total_janelas + carga_total_portas +  carga_total_pessoas + carga_total_aparelhos

    print( '''
    
CARGA TERMICA: ''',total_carga_termica_final,' Kcal/h')

    btu = total_carga_termica_final*3.92
    print('''
    
O total de BTUS é: ''', btu,''' 

''')
    
#TABELA PARA SABER QUAL AR CONDICIONADO  DEVE SER RECOMENDADO

    if btu <= 7500:
        btu = 7500
        modelo = (' Ar Condicionado Janela Mecânico Consul 220V CCB07EB ')
        preço = 999.90

        
    elif btu <= 9000:
        btu = 9000
        modelo = ('Ar Condicionado Split Hi Wall Fontaine FOFT09F2R4CON02 - 220 Volts ')
        preço =  1.213

        
    elif btu <= 10000:
        btu = 10000
        modelo = (' Ar condicionado Consul de janela frio 220V CCB10EBBNA  ')
        preço =  1.587

        
    elif btu <= 12000:
        btu = 12000
        modelo = (' Ar Condicionado Split Philco PAC12000TFM12 Frio - 220v')
        preço =  1.400

        
    elif btu <= 18000:
        btu = 18000
        modelo = ('Ar Condicionado Split Consul Hi Wall Frio CBN18CBBNA - 220V')
        preço = 2.058

        
    elif btu <= 24000 :
        btu = 24000
        modelo = ('Ar Condicionado Split Philco Frio Inverter 220V PAC24000IFM9W ')
        preço = 3.199

        
    elif btu <= 27000 :
        btu = 27000
        modelo = ('Ar Condicionado Split Inverter Fujitsu Quente e Frio High Wall')
        preço = 8.145

        
    elif btu <= 30000 :
        btu = 30000
        modelo = ('Ar Condicionado Split Elgin Eco Inverter Quente/Frio 220V ')
        preço = 4.948

        
    elif btu <= 36000 :
        btu = 36000
        modelo = ('Ar Condicionado Split Piso Teto Elgin EcoQuente E Frio – 220 Volts ' )
        preço = 6.189

        
    elif btu <= 48000:
        btu = 48000
        modelo = ('Ar Condicionado Split Teto Inverter LG Quente/Frio 220V' )
        preço =  10.823

        
    elif btu <= 60000:
        btu = 60000
        modelo = ( 'Ar Condicionado Split Piso Teto Inverter Gree Quente E Frio 220V ') 
        preço = 16.899 
    else:
        btu = 60000
        modelo = ( 'Ar Condicionado Split Piso Teto Inverter Gree Quente E Frio 220V ') 
        preço = 16.899 
        


    print (''' O ar condicionado recomendado para seu recinto é este:
        ''')
    print (' ____________________________________________________________________________________')
    print ('|CAPACIDADE BTU: ', btu)                                 
    print ('|____________________________________________________________________________________|')
    print ('|MODELO: ', modelo)              
    print ('|____________________________________________________________________________________|')
    print ('|VALOR: ', preço, ' R$')
    print ('|____________________________________________________________________________________|')
            


    input (''' 

    Obrigado e até a proxima! Clique enter para finalizar.''')
        


#INICIA O PROGRAMA
recinto()