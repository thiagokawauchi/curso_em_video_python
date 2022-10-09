from datetime import date
lista = []
for c in range(1, 8):
    lista.append(int(input(f'Em que ano a {c}ª pessoa nasceu? ')))

maiores = 0
menores = 0
for pessoa in lista:
    if date.today().year - pessoa >= 21:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade.')
print(f'E também tivemos {menores} pessoas menores de idade.')
