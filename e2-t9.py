from functools import reduce

# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

impares = filter( lambda num: num % 2 != 0, numeros )
sumatoria = reduce( lambda a, b: a + b, impares )
print( sumatoria )