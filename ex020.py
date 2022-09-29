from random import shuffle
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
alunos = [primeiro, segundo, terceiro, quarto]
shuffle(alunos)
print(f'A ordem de apresentação será \n{alunos}')
