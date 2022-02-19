print('\n\nBem-vindo ao seu assistente de senha segura')
#importação de pacotes random choice e string ASCII do Python
from random import choice
import string
#são criados duas variáveis contendo mensagens de iteração com o usuário...
mensagem_condicao = '\nATENÇÃO: \n* mínimo de 6 carateres. \n*pelo menos 1 dígito. \n*pelo menos 1 carater minúsculo. \n*pelo menos 1 carater maiusculo. \n*pelo menos 1 carater especial.'
mensagem_OK = '\nVERIFICAÇÂO: \n-mínimo 6 carateres... OK \n-pelo menos 1 dígito...OK \n-pelo menos 1 carater minúsculo... OK \npelo menos 1 carater maiusculo... OK \npelo menos 1 carater especial... OK'

senha = '' #a variável que irá armazenar a senha desejada
# foi criada uma função <gerar_senha> que irá aplicar o comando choices de nossa lista de strings (minusculos, maiusculos, números e carater especal)
def gerar_senha():
  senha_gerada =''
  tamanho = 10 #limitamos para 10 carateres na amplicação da função
  valores = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
  for i in range(tamanho):
      senha_gerada += choice(valores) #o loop repete até o máximo de 10 selecionando da lista de strings ASCII
  return senha_gerada

print(mensagem_condicao)
print('Digite uma senha de sua preferência:')
senha = str(input()) #o usuário informa a senha desejada
#primeira ieração <IF> confere se o tamanho é menor que 6 carateres
if (len(senha)<6):
  print('Entrada incompleta!!!  ... Não preocupe, geramos uma senha respeitando sua proposta original...\n')
  senha = senha + gerar_senha() #aqui o algoritmo "pega" a senha incompleta do usuário e a prenche com a função <gerar_senha>
  print(senha + '   (Salve num lugar seguro!)')
else: #caso contrário (a senha tem 6 ou mais carateres, verifica as demais condições solicitadas com um novo <if-else> aninhado...)
  if (any(chr.isdigit() for chr in senha) and any(chr.isupper() for chr in senha) and any(chr.islower() for chr in senha) and any(chr.isalpha() for chr in senha)):
    #caso a senha cumpra com as condições, uma mensagem de confirmação é exibida...
    print('\nParabens! ... Sua senha cumpre com as condições solicitadas \n' + mensagem_OK)
    print('\nSua nova senha é:', senha, '   (Salve num lugar seguro!)')
  else: #senão... (a senha tem 6 ou mais carateres, mas não cumpre com o resto das condições) o algoritmo irá gerar um novo
    print('\nsua senha não cumpre com as condições solicitadas\n' + mensagem_condicao)
    senha = gerar_senha()
    print('\n Foi gerada uma nova senha aleatória com sucesso:' , senha , '   (Salve num lugar seguro!)')

print('\nMuito obrigado!!!')
