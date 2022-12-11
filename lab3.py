def find_sum(m):
    return sum(m)

'''Ввод данных'''
m = list()
for i in range(10):
    m.append(int(input()))

print(find_sum(m))



def counting_zero(m):
    k = 0
    for i in range(len(m)):
        if m[i] == 0:
            k += 1
            return k

'''Ввод данных'''
m = list()
for i in range(10):
    m.append(int(input()))

print(counting_zero(m))



def stairs(m):
    for i in range(1, m + 1):
        l = ''
        for j in range(1, i + 1):
            l = l + str(j)
        print(l)
    return 'End'

'''Ввод данных'''
m = 0
m = int(input())

print(stairs(m))




def stairs(m):
    for i in range(1, m + 1):
        l = ''
        for j in range(1, i + 1):
            l = l + str(j)
        for j in range(i - 1, 0, -1):
            l = l + str(j)
        print(l)
    return 'End'

'''Ввод данных'''
m = 0
m = int(input())

print(stairs(m))
