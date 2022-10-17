expression = str(input('Digite a expressão: ')).replace(' ', '')
saldo_fechado = 0
for char in expression:
    if char == '(':
        saldo_fechado += 1
    elif char == ')':
        saldo_fechado -= 1
        if saldo_fechado < 0:
            break
if saldo_fechado != 0:
    print(f'Sua expressão está errada!')
else:
    print(f'Sua expressão está válida!')
