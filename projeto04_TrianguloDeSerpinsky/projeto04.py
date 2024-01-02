import math


def Factorial(x):
    if x == 0:
        return 1
    elif x < 0:
        return print('x negativo')
    else:
        return int(x * Factorial(x-1))


def COMBINATION(n, p):
        result = Factorial(n) / (Factorial(p) * Factorial(n - p))
        return result


def PARouIMPAR(p):
    return True if p / 2 == 0 else False


def output_to_file(text):
    with open('fatoriais.txt', 'a') as file:
        file.write(str(text) + '\n')
    file.close()


'''n = 50
logs = 0
for p in range(1, n+1):
    logs += math.log(p, 10)
'''