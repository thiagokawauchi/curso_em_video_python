from time import sleep
while True:
    sistema = f'{"SISTEMA DE AJUDA PyHELP"}'
    print('\033[m\033[1;42m~' * (len(sistema) + 4))
    print(f'  {sistema}  ')
    print('~' * (len(sistema) + 4))
    sleep(1)
    option = str(input('\033[mFunção ou Biblioteca (fim para encerrar) > ')).strip().lower()
    if option == 'fim':
        ate = 'ATÉ LOGO!'
        print('\033[1;41m~' * (len(ate) + 4))
        print(f'  {ate}  ')
        print('~' * (len(ate) + 4))
        break
    else:
        access_msg = f"Acessando o manual do comando '{option}'"
        print('\033[1;44m~' * (len(access_msg) + 4))
        print(f'  {access_msg}  ')
        print('~' * (len(access_msg) + 4))
        sleep(1)
        print(end='\033[m\033[7;40m')
        help(option)
        sleep(2)
