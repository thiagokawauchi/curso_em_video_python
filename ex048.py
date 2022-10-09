valores = 0
total = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        valores += 1
        total += c
print(f'A soma de todos os {valores} valores solicitados é {total}')