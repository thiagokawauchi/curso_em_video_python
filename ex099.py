from time import sleep


def maior(* number):
    print('-=-' * 20)
    print('Analisando os valores passados...')
    sleep(0.5)
    for i in number:
        print(i, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(number)} valores ao todo.')
    sleep(0.5)
    if number == ():
        number = (0,)
    print(f'O maior valor informado foi {max(number)}.')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
