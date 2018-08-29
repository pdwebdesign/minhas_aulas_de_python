#https://blog-luz-vc.cdn.ampproject.org/c/s/blog.luz.vc/excel/como-fazer-media-mediana-e-desvio-padrao-excel/amp/
#https://pt.wikipedia.org/wiki/Desvio_padr%C3%A3o
#https://www.todamateria.com.br/desvio-padrao/
#http://www.igm.mat.br/cursos/a_linear/matrizes/produto2.htm
import numpy as np


if True:
    numeros = [1,2,6,6,5,3]
    print("MEDIA DO ARRAY:")
    media = np.mean(numeros)
    print(media)

    '''
    É importante ressaltar que quando temos uma quantidade 
    ímpar de números, definimos a mediana como o número central
    dos números apresentados conforme mostrado acima. 
    Porém quando se tem uma quantidade par de números, 
    definimos a mediana destes são definidas da seguinte forma: 
    Somam-se os dois números centrais e calcula-se a media entre eles.
    '''

    print("MEDIANA DO ARRAY:")
    mediana = np.median(numeros)
    print(mediana)

    '''Dentro da estatística, o termo desvio de padrão tem como 
    objetivo demonstrar a regularidade referente a um conjunto de 
    dados de modo a apontar o grau de oscilação destes em comparação
    com a média dos valores do conjunto.'''


    print("DESVIO PADRAO DO ARRAY:")
    desvio = np.std(numeros)
    print(desvio)
    print("-------------\n")

'''
O código a seguir é para ajudá-lo a começar com o Numpy, que é uma biblioteca
que fornece funções que são especialmente úteis quando você precisa
trabalhar com grandes matrizes e matrizes de dados numéricos, como fazer
multiplicações matriciais. Além disso, Numpy é testado em combate e
otimizado para funcionar rápido, muito mais rápido do que se você estivesse trabalhando
com listas do Python diretamente.
'''

'''
A classe de objeto de matriz é a base do Numpy, e matrizes Numpy são como
listas em Python, exceto que cada coisa dentro de uma matriz deve ser do
mesmo tipo, como int ou float.
'''
# Altere False para True para ver as matrizes Numpy em ação
if False:
    print("PRIMEIRO EXEMPLO:")
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
    print(array)
    print("-----------------")

'''
Você pode indexar, fatiar e manipular um array Numpy como faria com um
uma lista do Python.
'''
# Altere False para True para ver a indexação de matriz e o fatiamento em ação
if False:
    print("SEGUNDO EXEMPLO:")
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    print(array[1])
    print("")
    print(array[:2])
    print("")
    array[1] = 5.0
    print(array[1])
    print("-----------------")
# Altere False para True para ver a indexação de matriz e o fatiamento em ação
if False:
    print("TERCEIRO EXEMPLO:")
    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print(two_D_array)
    print("")
    print(two_D_array[1][1])
    print("")
    print(two_D_array[1, :])
    print("")
    print(two_D_array[:, 2])
    print("-----------------")

'''
Aqui estão algumas operações aritméticas que você pode fazer com matrizes Numpy
'''
# Mude False para True para ver Arithmetics Array in action
if False:
    print("OPERAÇÕES ARITMETICAS:")
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    print(array_1 + array_2)
    print("")
    print(array_1 - array_2)
    print("")
    print(array_1 * array_2)
    print("-----------------")
# Mudar False para True para ver a aritmética da Matriz em ação
if False:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print("SOMAR:")
    print(array_1 + array_2)
    print("SUBTRAIR:")
    print(array_1 - array_2)
    print("MULTIPLICAR:")
    print(array_1 * array_2)

'''
Além das operações aritmeticas padrão, a Numpy também possui uma gama de
outras operações matemáticas que você pode aplicar aos arrays Numpy, 
'''
if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    print(np.mean(array_1))
    print(np.mean(array_2))
    print("")
    print("Produto escalar")
    print(np.dot(array_1, array_2))
