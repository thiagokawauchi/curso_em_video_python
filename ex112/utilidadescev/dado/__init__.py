def leiaDinheiro(msg):
    while True:
        p = str(input(msg)).strip().replace(',', '.')
        p_without_dots_and_commas = p.replace('.', '').replace(',', '')
        if p_without_dots_and_commas.isnumeric():
            break
        else:
            print(f'\033[31mERRO: "{p}" é um preço inválido!\033[m')
    p = float(p)
    return p
