#	Normal: tempoChegada <= 0 ; Atraso: tempoChegada > 0

Atraso = False
tempoChegada = []

#solicita ao professor para informar qual é o limite do dia:
x = int(input('\nDigite o numero limite de alunos para avaliar: '))
#Quantos alunos estão presentes no momento da consulta?
y = int(input('\nIndique quantidade de alunos na sala: '))

#verificação se o limite é menor ou igual à quantidade de alunos na sala
if x <= y: #o algoritmo continua somente se o limite for pelo menos igual ao numero de alunos presentes
    for i in range(y):
        z = int(input('Digite sucessivamente o tempo de cada aluno: '))
        tempoChegada.append(z)

    tempoChegada.sort() #ordenamos os tempos
    print('\nLista ordenada,com o tempo de todos os alunos: ', tempoChegada)
    
    print('\nResultado para o  limite de {} entre {} alunos:'.format(x, y))

    for i in range(x):
        if tempoChegada[i] <=0: #imprime quais alunos chegaram com tempo normal dentro da amostra (quantidade limite)
            print('Aluno', i, 'OK, com tempo:', tempoChegada[i])
        else: #a condição não foi satisfeita, caso qualquer aluno dentro do limite 'x' estiver fora do tempo normal
            Atraso = True #nesse caso, a condição Atraso muda para True, e imprime qual(is) aluno(s) chegaram fora do limite
            print('Aluno', i, 'Atrasado, com tempo:', tempoChegada[i])

#verificação da variável Atraso para informar a situação:
    if Atraso == False:
        print('\nResultado: Aula normal')
    else:
        print('\nResultado: Aula cancelada')
else: #caso o professor informe um limite superior à quantidade de alunos na sala
    print('\nConfirma! O limite deve ser menor ou igual ao numero de alunos na sala')
