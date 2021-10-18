import os

f1 = open('1.txt', 'r', encoding="utf-8")
s11 = f1.readlines()
s1 = len(s11)

f2 = open('2.txt', 'r', encoding="utf-8")
s22 = f2.readlines()
s2 = len(s22)

f3 = open('3.txt', 'r', encoding="utf-8")
s33 = f3.readlines()
s3 = len(s33)

data = [s1, s2, s3]
valu = [s11, s22, s33]
result = dict(zip(data, valu))

sorted_dict = {}
sorted_keys = sorted(result)
for w in sorted_keys:
    sorted_dict[w] = result[w]


with open('Итог.txt', 'w', encoding="utf-8") as file:
    for key, value in sorted_dict.items():
        file.write(f'{key}\n, {value}\n')

