"""
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
"""
s1 = [i for i in range(1, 21, 2)]
print(f'a) {s1}')

s2 = [2]

for _ in range(0, 9):
    s2.append(s2[-1] * 2)

print(f'b) {s2}')

s3 = [i ** 2 for i in range(0, 11)]
print(f'c) {s3}')

s4 = [i ** 2 * 4 for i in range(1, 11)]
print(f'd) {s4}')

s5 = [1, 1]

for _ in range(0, 8):
    s5.append(s5[-1] + s5[-2])

print(f'e) {s5}')

s6 = [2, 10, 12] + [i for i in range(16, 26)]
print(f'f) {s6}')
