import math
lado = float (input())
areatriangulo = ((lado ** 2) * math.sqrt(3)) / 4
areahexagono = (areatriangulo * 6)
perimetrohexagono = lado * 6
print (f'Lado do hexagono: {lado} metros,')
print (f'Area: {areahexagono} metros quadrados,')
print (f'Perimetro: {perimetrohexagono} metros.')
