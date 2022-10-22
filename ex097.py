def escreva(text):
    text_len = len(text)
    line_len = text_len + 4
    print('~' * line_len)
    print(f'  {text}  ')
    print('~' * line_len)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
