def voto(born):
    from datetime import date
    idade = date.today().year - born
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


nascimento = int(input('Em que ano você nasceu? '))
voto_status = voto(nascimento)
print(voto_status)
