import sympy
from numpy import random
from fractions import Fraction
import time

class MatrixException:
    pass

def generate_A(n=2):
    matrix = [[random.randint(-5, 5) for i in range(n)]for k in range(n)]
    return matrix


def transpose(mtx):
    return [list(i) for i in zip(*mtx)]


def foo(mtx, i=0, q=None):
    if i == len(mtx):
        return q
    if i == 0:
        under_sqrt = sum(j ** 2 for j in mtx[i])  # знаменатель q_1
        q = [[Fraction(k, 1) * (1 / sympy.sqrt(under_sqrt)) for k in mtx[i]]]  # считается столбец q_1
    else:
        sum_under_sqrt = 0  # то, что получается под корнем (сумма квадратов каждого значения a_энного) для q_энного (n>=1)
        a_p = []  # список элементов в a_энном_перпендикулярном
        scalar = []  # скалярное произведение <a_n,q_k>q_k
        scalar_sum = []
        for g in range(len(q)):
            scalar.append([sum(mtx[i][k] * q[g][k] for k in range(len(mtx))) * q[g][j] for j in range(len(mtx))])
        summa = scalar[0]
        if i > 1:
            for j in range(len(mtx)):
                for k in range(1, len(scalar)):
                    summa[j] += scalar[k][j]
        scalar_sum.append(summa)
        for j in range(len(mtx)):
            t = (mtx[i][j] - scalar_sum[0][j])
            a_p.append(t)
            sum_under_sqrt += t ** 2
        s = 1 / sympy.sqrt(sum_under_sqrt)
        q.append([s * a_p[k] for k in range(len(mtx))])
    return foo(mtx, i + 1, q)


def printer(mtx):
    try:
        mtx = transpose(mtx)
        for i in range(len(mtx)):
            for k in range(len(mtx)):
                print(mtx[i][k], '  ', end='')
            print()
    except:
        raise MatrixException


def generateQ(n):
    return foo(generate_A(n))


start_time = time.time()
printer(generateQ(100))
print("--- %s seconds ---" % (time.time() - start_time))