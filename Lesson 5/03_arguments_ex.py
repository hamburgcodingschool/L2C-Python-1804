def multTable(number):
    for i in range(1, 11):
        res = number * i
        print('{} X {} = {}'.format(number, i, res))

for i in range(1, 6):
    multTable(i)
    print("-----------")