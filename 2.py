"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a
sequência.
"""
n = int(input('Insira o valor que deseja analisar: '))
atual = 0
fibonacci = [0]

while True:
    if n == atual:
        print(f'O valor {n} está contido na sequência de Fibonacci.')
        print(f'A sequência até o valor inserido: {fibonacci}')
        break
    elif n < atual:
        print(f'O valor {n} não está contido na sequência de Fibonacci.')
        break
    else:
        if atual == 0:
            atual = 1
            fibonacci.append(atual)
        else:
            atual = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(atual)
