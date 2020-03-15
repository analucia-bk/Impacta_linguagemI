import math
areautilizada = float(input())
quantidade24L = areautilizada/ (24 * 7)
valor24L = math.ceil(quantidade24L) * 91
total24L = math.floor(areautilizada / (24 * 7))

quantidade5L = areautilizada / (5.4 * 7)
valor5L = math.ceil(quantidade5L) * 23
total5L = math.ceil((areautilizada % (24 * 7)) / (5.4 * 7))

valorfinal = (total24L * 91) + (total5L * 23)

print(f"a) {math.ceil(quantidade24L)} lata(s) de 24 litros: R$ {valor24L:.2f}")
print(f"b) {math.ceil(quantidade5L)} lata(s) de 5.4 litros: R$ {valor5L:.2f}")
print(f"c) {total24L} lata(s) de 24 litros e {total5L} lata(s) de 5.4 litros: R$ {valorfinal:.2f}")