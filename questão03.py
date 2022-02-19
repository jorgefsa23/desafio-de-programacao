# solicitamos ao usuário para informar a palavra (string de entrada)
print('\nInsira palavra:')
palavra = str(input())
tamanho = len(palavra) # armazenamos sua extensão para utilizar nos loops
print('Contem', tamanho, 'letras') #mensagem de iteração com o usuário

sub_strings=[] # criamos uma lista onde serãoarmazenadas as entradas da sub_string solicitada
# inicializamos variáveis auxiliáres de iteração da nossa string
i=0
j=1
while i <= (tamanho-1):
    while j <= tamanho:
        fatia = palavra[i:j] # aqui a palavra é fatiada (slicing) comezando com a letra inicial (posição i=0), até a segunda posição (j=1)
        sub_strings.append(fatia) #cada uma das "fatias" são armazanadas na lista <sub_strings> com o comando .append() 
        j = j+1 # acrecentamos j em 1, para ir aumentando o tamanho da fatia, até a última letra da palavra (=tamanho)
    i = i+1 # finalizada a interação da variável j até cobrir a última letra, o loop "sai" para o while principal
    j = j=i+1 # j também aumenta em 1 para iniciar na letra subsequente de i
# finalizado o loop anterior, temos completado nossa lista de sub_strings (primeira parte do problema resolvido)
print('\nsendo o respetivo conjunto de sub_strings:')
print(sub_strings)
print('São', len(sub_strings) , 'elementos criados no conjunto de sub_strings')

### segunda parte... verificação de anagramas das sub_strings...

# A lista <sub_string> e armazenado numa lista auxiliar:
auxiliar = sub_strings
anagramas = [] #inicializamos nossa lista de anagramas
# a função anagram_checker verifica cada palavra com os elementos de uma lista
def anagram_checker(entrada, lista):
    iguais = ''
    for palavra in lista:
        if sorted(palavra) == sorted(entrada): #aqui, o comando <sorted> cria uma lista ordenada com cada letra das palavras, caso sejam iguais, são anagramas
            iguais = entrada + ' & ' + palavra # se encontrar anagramas, armazena na variável iguais
            anagramas.append(iguais) # se encontró anagramas, a lista <anagramas> será atualizado
    return anagramas # a saída da função, e a lista de anagramas atualizada

# a variavel auxiliar l armazena a extensão da nossa auxiliar, serve para as interações com o seus elementos
l = len(auxiliar)
while l > 0:
    l = l - 1 # a variável l irá diminuir até o valor zero, neste caso, o primeiro elemento da lista auxiliar
    x = auxiliar.pop() #a variável x armazena um elemento por vez, sendo eliminando ele da lista auxiliar <.pop() elimina o último elemento>
    result = anagram_checker(x,auxiliar) #aqui é chamado a função <anagram_checker>, cada vez que a variável x extrair um elemento da lista <auxiliar>
#finalizada a verificação de anagramas, temos uma última confirmação...
#este último <if-else> verifica se a lista <result> tem elementos, caso sim, será exibida os anagramas encontrados
if result:
    print('\n>>> Esta lista de sub-strings tem os seguintes Anagramas:\n', result)
else: #caso <result> esteja vazia, significa que não foram encontrados anagramas...
    print('>>> Esta lista de sub-strings não tem anagramas')

print('\nMuito obrigado!')
