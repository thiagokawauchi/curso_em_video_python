print('-' * 40)
print('Sequência de Fibonacci')
print('-' * 40)
termos = int(input('Quantos termos você quer mostrar? '))
print('~' * 40)
counter = 0
fibo = []
while counter < termos:
    if counter == 0:
        fibo.append(0)
        print(f'{fibo[0]} → ', end='')
    elif counter == 1:
        fibo.append(1)
        print(f'{fibo[1]} → ', end='')
    else:
        fibo.append(fibo[len(fibo) - 1] + fibo[len(fibo) - 2])
        print(f'{fibo[len(fibo) - 1]} → ', end='')
    counter += 1
print('FIM')
print('~' * 40)

#Solução Guanabara
c = 3
t1 = 0
t2 = 1
t3 = t1 + t2
print(f'{t1} → {t2} → ', end='')
while c <= termos:
    print(f'{t3} → ', end='')
    c += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')
print('~' * 40)
