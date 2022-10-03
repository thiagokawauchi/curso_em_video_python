number = int(input('\033[35mMe diga um número qualquer: \033[m'))
if number % 2 == 0:
    print(f'O número {number} é \033[34mPAR\033[m')
else:
    print(f'O número {number} é \033[34mÍMPAR\033[m')
