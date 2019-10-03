prime_number=[]
for i in range (2, 1000):
    flag = 0
    for num in prime_number:
        if i % num == 0:
            flag = 1
    if flag == 0:
        prime_number.append(i)
print(prime_number)


mylist = [4, 0, 5, -5, 6, 2, 9, 1, 19, 34, 20, 1, 35, 35, 322]
print(mylist)
def sel_choice(x):
    length = len(x)
    min = x[0]
    for j in range(length):
        for i in range(j, length):
            min = x[j]
            if x[i] <= min:
                min = x[i]
                x[j], x[i] = x[i], x[j]
sel_choice(mylist)
print(mylist)    
