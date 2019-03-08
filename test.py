def normalize(temp: list, span: int):
    master_index = 0
    compared_index = 0



    print(temp)


temp = [[1604, 872], [1682, 876], [1681, 970], [1602, 968]]
temp.sort(key=lambda x: x[1])

normalize(temp, 5)

for item in temp:
    item[1] = temp[0][1]