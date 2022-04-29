
number, reverse, sum = 0, 0, 0
pares = [] #lista temporal para armazanar todos os casos encontrados
resultantList = [] #lista final, após verificação de casos repetidos
i = 11 #iniciamos em 11, pois de 0 a 10 não pode ter reverso

#condição > a soma ser inferior a 1 milhão
while sum < 1000000:
    number = i
    novo = ''
    reverse = int(str(number)[::-1]) #criamos o reverso de n, fazendo o reverso da sua string e transformando a seguir em inteiro
    
    #se a soma dividido por 2 for tiver resto e se forem do mesmo conjunto
    #a segunda condição elimina casos como considerar que 770 tem o reverso 77
    if ((number + reverse) % 2 != 0) and (len(str(number)) == len(str(reverse))):
        #aqui a soma para verificar:
        sum = number + reverse
        if sum < 1000000: #somente se for menor a 1 milhão
            #este if-else para ordenar sempre o menor pela frente e poder eliminar duplicados no próximo passo
            if number > reverse:
                novo = str(reverse) +' e ' + str(number)
            else:
                novo = str(number) +' e ' + str(reverse)
            #salvamos todos os pares numa lista de pares:
            pares.append(novo)
    i = i + 1
#eliminando duplicados, exeplo: o par '12 e 21', volta a repetir quando o algoritmo analiza '21 e 12'
for element in pares:
    if element not in resultantList:
        resultantList.append(element)

#impresão de resultado final:
print('***** Resultado: *****')
print(resultantList)
print('Total de pares de numeros encontrados: {}'.format(len(resultantList)))