#importamos 'combinations_with_replacement' do pacote intertools, para fazer as combinações de elementos
from itertools import combinations_with_replacement

print('\n\nAlgoritmo para imprimir todos os subcojuntos do vetor v, onde a soma dos elementos for igual a um numero n')

n = int(input('\nDigite o valor de n: '))
extensao = int(input('\nDigite o numero de elementos da lista: '))
lista = [] #objeto para armazenar a lista original a ser informada pelo usuário
aux = [] #para armazenar todos os subconjuntos possíveis
final = [] #armazena o resultado final que satisfaz as condições do desafio

#informar os elementos da lista:
for i in range(extensao):
    valor = int(input('Insira valor:  '))
    lista.append(valor)

listaOrdenada = sorted(lista) #para garantir que os elementos da lista estejam de forma crescente 
print('lista original com elementos ordenados:' , listaOrdenada)

maximo = int(n/(listaOrdenada[0])) #a máxima extensão possível = n / valor do menor elemento
print('Máxima combinação possivel de elementos:', maximo)

#função para calcular soma de elementos de uma lista:
def somaElementos(lista):
    soma = 0
    for elementos in lista:
        soma = soma + elementos
    return soma

maisCurto = maximo #inicia a solução do algoritmo como a extensão da lista mais comprida, para comparar e achar o mais curto

for x in range(1, maximo+1): #percorre a lista
    temp = list(combinations_with_replacement(listaOrdenada, x)) #faz a combinação de elementos desde range=1 até o elemento final da lista
    #ainda encima: 'combinations_with_replacement' permite repetir elementos
    for i in temp: #para cada grupo de combinações, percorre a lista temporar resultantes
        if somaElementos(i) == n: #verifica se a soma dos elementos é igual a n
            aux.append(i)     #caso sim, adiciona na list auxiliar
            extensao = len(i) #verifica a extensão das listas selecionadas
            if extensao < maisCurto: #caso seja menor a 'maisCurto', ele será armazenado como novo 'menor' valor
                maisCurto = extensao

#apresentação dos resultados parciais
print('*'*20)
print('Lista parcial com todos os conjuntos possiveis:', aux)
print('*'*20)
print('Menor numero de elementos nas listas resultantes:', maisCurto)

#da lista aux, selecionamos os que tem a extensão equivalente a 'maisCurto'
for elements in aux:
    if len(elements) == maisCurto:
        elements = list(elements) #aqui transforma as tuplas em lista, pois a condição do desafio é apresentar resultado como conjunto de listas
        final.append(elements)

#exibição do resultado final:
print('\n********* RESULTADO FINAL: *********')
print('\nConjunto de listas mostrando os de menor elemento:', final)

