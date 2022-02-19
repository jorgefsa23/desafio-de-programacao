print ('\nBem-vindo! \n Sou seu assistente para desenhar uma escada!!!\n')
#solicitamos ao usuário que informe a altura para a escada, limitando ao máx de 20...
print('Informe altura desejada (valor entre 1 e 20): ', end='');
#a variável h de tipo inteiro armazena a altura...
h = int(input());

#caso o valor seja fora do parâmetro, o usuário deve repetir...
while(h<1 or h > 20):
  print("Entrada invalida!!!, digite valor entre 1 e 20")
  print('Informe altura: ', end='');
  h = int(input());

#uma vez obtido uma entrada válida, o programa segue para a etapa de design...
print('\n\n Sua escada com altura <', h ,'> fica assim:')
#usamos a sintaxe <range(stop)> na estrutura de repetição <for>...lembrando que range conta até (n-1)
#exemplo, para n=3; range=0, 1, 2
for i in range(h):
     print(" " * (h - (i+1)) + "*" * (i + 1));
     #NOTA DESCRITIVA:
     #como <i> começa em 0; na primeira linha teremos "h-1" espaços em branco e "1" asterisco
     #na segunda linha <i=1>; então são "h-2" espaços em branco e "2" asteriscos
     #a contagem segue, assim; na última linha temos "h-h)" espaços em branco e "h" asteriscos
print('\nMuito obrigado!!!')